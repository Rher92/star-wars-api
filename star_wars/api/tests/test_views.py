from django.test import TestCase, Client
from django.urls import reverse
from api.views import RetrieveCharacter, SaveRating
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.character = {
            "name": "Luke Skywalker",
            "height": "172",
            "mass": "77",
            "hair_color": "blond",
            "skin_color": "fair",
            "eye_color": "blue",
            "birth_year": "19BBY",
            "gender": "male",
            "homeworld": {
                "name": "Tatooine",
                "population": "200000",
                "known_residents_count": 10
            },
            "species_name": [],
            "average_rating": 0.0,
            "max_rating": 0
        }

    def test_get_character(self):
        url = reverse('get_character', args=['1'])
        
        response = self.client.get(url)
        data = response.json()
        status = response.status_code

        self.assertEquals(self.character, data)
        self.assertEquals(200, status)

    def test_get_character_fail(self):
        character = 101001010000000000000000000000000000000000000
        url = reverse('get_character', args=[f'{character}'])
        error = {'message': f'does not exist character whit id:{character}'}

        response = self.client.get(url)
        data = response.json()
        status = response.status_code

        self.assertEquals(error, data)
        self.assertEquals(400, status)

    def test_save_qualification_for_an_user(self):
        character = 1
        qualify = 5
        message = {'message': 'success'}
        self.character['average_rating'] = 5
        self.character['max_rating'] = 5
        url = reverse('save_rating', args=[character, qualify])

        response = self.client.post(url)
        data = response.json()
        status = response.status_code

        self.assertEquals(message, data)
        self.assertEquals(200, status)

    def test_save_qualification_for_an_user_which_doesnot_exist(self):
        character = 101001010000000000000000000000000000000000000
        qualify = 5
        message = {'message': f'this id:{character} does not exist'}
        url = reverse('save_rating', args=[character, qualify])

        response = self.client.post(url)
        data = response.json()
        status = response.status_code

        self.assertEquals(message, data)
        self.assertEquals(400, status)


        