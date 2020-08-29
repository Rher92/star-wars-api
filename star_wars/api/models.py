from django.db import models


class CharacterEvaluations(models.Model):
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'rating{self.rating}'


class Characters(models.Model):
    ratings = models.ForeignKey(CharacterEvaluations,
        related_name='character',
        related_query_name='character',
        on_delete=models.CASCADE,
    )
    cid = models.IntegerField(unique=True)
    average_rating = models.FloatField()
    max_rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'character id: {self.cid}'

