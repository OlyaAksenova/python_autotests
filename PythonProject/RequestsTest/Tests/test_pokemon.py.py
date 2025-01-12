import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b418c528950bc721a582cecd90ad7a4d'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 14752

def test_status_code():
     response = requests.get(url=f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
     assert response.status_code == 200

def test_trainer_name():
   response_get = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID}) 
   assert response_get.json()["data"][0]["trainer_name"] == "Стив"
