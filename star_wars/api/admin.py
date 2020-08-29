from django.contrib import admin
from api.models import CharacterEvaluations, Characters


@admin.register(CharacterEvaluations)
class CharacterEvaluationsAdmin(admin.ModelAdmin):
    pass


@admin.register(Characters)
class CharactersAdmin(admin.ModelAdmin):
    pass