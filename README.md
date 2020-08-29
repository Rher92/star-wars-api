# star-wars-api

### Description

Star wars API is an API which can be consult Characters of that Fiction World, and too you could qualify the Characters.

This API relies on https://swapi.dev/


### Requirements

The only one requirement necessary is to have installes docker and docker-compose for running all containers


### how to build and run this API

first you have to clone the repository:

    - git clone https://github.com/Rher92/star-wars-api.git

If you want to see all logs running in realtime on the terminal, you must execute:
    - docker-compose up --build

But if you don't see the logs, execute:
    - docker-compose up --build -d

if the images already built and only you want to run them, you see the command above but you should take --build flag out.


### how to run tests

the command below execute all test:

docker-compose exec api python /usr/src/app/star_wars/manage.py test api


### Endpoints Descriptions

Getting some character:

http://127.0.0.1:8000/api/character/<character_id>


Saving qualification for an character:
http://127.0.0.1:8000/api/character/<character_id>/rating/<rating>


<character_id> : ID of the character
<rating>: Rating whitin a range between 1 and 5 points


### How to execute any Django command

docker-compose exec api python /usr/src/app/star_wars/manage.py <command>

command's examples:
createsuperuser

docker-compose exec api python /usr/src/app/star_wars/manage.py createsuperuser

