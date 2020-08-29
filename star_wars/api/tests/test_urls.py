from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api.views import RetrieveCharacter, SaveRating
from django.urls.exceptions import NoReverseMatch

class TestUrls(SimpleTestCase):

    def test_retrieve_character_resolved(self):
        url = reverse('get_character', args=['1'])
        self.assertEquals(resolve(url).func.view_class, RetrieveCharacter)

    def test_retrieve_character_without_args(self):
        exception = "Reverse for 'get_character' with no arguments not found. " \
            "1 pattern(s) tried: ['api/character/(?P<id>[0-9]+)$']"
        with self.assertRaises(NoReverseMatch) as context:
            url = reverse('get_character')
        self.assertEquals(exception, context.exception.args[0])

    def test_retrieve_character_args_errors(self):
        exception = "Reverse for 'get_character' with arguments '('a',)' not found. " \
            "1 pattern(s) tried: ['api/character/(?P<id>[0-9]+)$']"
        with self.assertRaises(NoReverseMatch) as context:
            url = reverse('get_character', args=['a'])
        self.assertEquals(exception, context.exception.args[0])

    def test_save_rating_resolved(self):
        url = reverse('save_rating', args=['1', '3'])
        self.assertEquals(resolve(url).func.view_class, SaveRating)

    def test_save_rating_without_args(self):
        exception = "Reverse for 'save_rating' with no arguments not found." \
            " 1 pattern(s) tried: ['api/character/(?P<id>[0-9]+)/rating/(?P<rating>[0-9]+)$']"
        with self.assertRaises(NoReverseMatch) as context:
            url = reverse('save_rating')
        self.assertEquals(exception, context.exception.args[0])
     
      