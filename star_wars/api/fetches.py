import requests 
from django.conf import settings


CHARACTER_ENDPOINT = settings.FETCH_PEOPLE_API


def verify_user(cid):
    _return = False
    if type(cid) is int:
        endpoint = CHARACTER_ENDPOINT + str(cid)
        r = requests.get(endpoint)
        if r.ok:
            _return = True
    return _return
    

def _fetch_character(cid):
    character = None
    hw_endpoint = None
    spec_endpoint = None
    if type(cid) is int:
        endpoint = CHARACTER_ENDPOINT + str(cid)
        r = requests.get(endpoint)
        if r.ok:
            character = r.json()
            hw_endpoint = character.get('homeworld')
            spec_endpoint = character.get('species')
    return character, hw_endpoint, spec_endpoint


def _fetch_homeworld(hw_endpoint):
    homeworld = None
    if hw_endpoint:
        r = requests.get(hw_endpoint)
        if r.ok:
            homeworld = r.json()
    return homeworld


def _fetch_specie(spec_endpoint):
    specie_lyst = []
    if spec_endpoint:
        for endpoint in spec_endpoint:
            r = requests.get(endpoint)
            if r.json():
                specie = r.json()
                specie_lyst.append(specie.get('name'))
    return specie_lyst


def _populate_character(character_json, homeworld_json, specie_lyst):
    if homeworld_json:
        _homeworld = HomeWorld()
        for element in homeworld_json.keys():
            if element in dir(_homeworld):
                setattr(_homeworld, element, homeworld_json.get(element))
        _homeworld.known_residents_count = homeworld_json.get('residents').__len__()

    _character = Character()
    for element in character_json.keys():
        if element in dir(_character):
            setattr(_character, element, character_json.get(element))
    
    _character.species_name = specie_lyst
    _character.homeworld = _homeworld

    return _character
   

def fetch(cid):
    _return = None
    character_json, hw_endpoint, spec_endpoint = _fetch_character(cid)
    if character_json:
        homeworld_json = _fetch_homeworld(hw_endpoint)
        specie_lyst = _fetch_specie(spec_endpoint)
        _return = _populate_character(character_json, homeworld_json, specie_lyst)
    return _return
        

class Character:
    def __init__(self):
        self.name = None
        self.height = None
        self.mass = None
        self.hair_color = None
        self.skin_color = None
        self.eye_color = None
        self.birth_year = None
        self.gender = None
        self.homeworld = None
        self.species_name = None
        self.average_rating = 0
        self.max_rating = 0


class HomeWorld:
    def __init__(self):
        self.name = None
        self.population = None
        self.known_residents_count = 0

