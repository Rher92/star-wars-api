from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from api.fetches import fetch
from api.serializers import BringCharacterSerializer
from api.services import save_character, save_character_evaluation
from api.validators import SaveRatingValidator
from api.selectors import retrieve_character


class RetrieveCharacter(APIView):
    def get(self, request, id):
        if not (character := cache.get(id)):
            character = fetch(id)
            cache.set(id, character)

        response = {'message': f'does not exist character whit id:{id}'}
        status = 400
        
        if character:
            if (_character := retrieve_character(id)):
                character.max_rating = _character.max_rating
                character.average_rating = _character.average_rating         
            serializer = BringCharacterSerializer(character)
            response = serializer.data
            status = 200
        
        return Response(response, status=status)


class SaveRating(APIView):
    def post(self, request, id, rating):
        validator = SaveRatingValidator(id, rating)
        response = validator.message
        status = validator.status
        
        if validator.is_valid:
            rating_obj = save_character_evaluation(rating)
            character = save_character(id, rating_obj)

            if (_character := cache.get(id)):
                _character.average_rating = character.max_rating
                _character.max_rating = character.average_rating
                cache.set(id, _character)
        
        return Response(response, status=status)
