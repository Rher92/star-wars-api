from django.test import TestCase
from api.models import CharacterEvaluations, Characters
from api.services import save_character

class TestModels(TestCase):

    def setUp(self):
        self.cid = 1
        self.eval = CharacterEvaluations.objects.create(
            rating=4
        )
        self.character = Characters.objects.create(
            ratings=self.eval,
            cid=self.cid,
            average_rating=self.eval.rating,
            max_rating=self.eval.rating,
        )

    def test_properties_eval_resolved(self):
        self.assertEquals(self.eval.rating, 4)

    def test_properties_character_resolved(self):
        self.assertEquals(self.character.cid, 1)
        self.assertEquals(self.character.ratings, self.eval)
        self.assertEquals(self.character.average_rating, 4)
        self.assertEquals(self.character.max_rating, 4)

    def test_add_new_eval(self):
        second_eval = CharacterEvaluations.objects.create(
            rating=3
        )
        character = save_character(
            self.cid,
            second_eval,
        )

        self.assertEquals(character.average_rating, 3.5)
        self.assertEquals(character.max_rating, 4)