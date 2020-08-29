from rest_framework import serializers


class BringHomeWorldSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    population = serializers.CharField(max_length=40)
    known_residents_count = serializers.IntegerField()


class BringCharacterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    height = serializers.CharField(max_length=40)
    mass = serializers.CharField(max_length=40)
    hair_color = serializers.CharField(max_length=40)
    skin_color = serializers.CharField(max_length=40)
    eye_color = serializers.CharField(max_length=40)
    birth_year = serializers.CharField(max_length=40)
    gender = serializers.CharField(max_length=40)
    homeworld = BringHomeWorldSerializer(required=False)
    species_name = serializers.ListField()
    average_rating = serializers.FloatField()
    max_rating = serializers.IntegerField()
    