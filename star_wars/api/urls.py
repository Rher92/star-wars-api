from django.urls import path
from .views import RetrieveCharacter, SaveRating

urlpatterns = [
    path('character/<int:id>', RetrieveCharacter.as_view(), name='get_character'),
    path('character/<int:id>/rating/<int:rating>', SaveRating.as_view(), name='save_rating'),
]