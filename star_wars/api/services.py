from __future__ import division
from api.models import CharacterEvaluations, Characters
from api.selectors import retrieve_character


def save_character_evaluation(rating):
    evaluation = CharacterEvaluations(rating=rating)
    evaluation.save()
    return evaluation


def save_character(cid, rating_obj):
    if not (character := retrieve_character(cid)):
        character=Characters(
            cid=cid,
            ratings=rating_obj,
            average_rating=rating_obj.rating,
            max_rating=rating_obj.rating
        )
    else:
        rating = rating_obj.rating
        character.rating = rating
        character.average_rating = (character.average_rating + rating) / 2
        if rating_obj.rating > character.max_rating:
            character.max_rating = rating
    character.save()
    
    return character