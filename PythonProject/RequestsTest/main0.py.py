import requests


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b418c528950bc721a582cecd90ad7a4d'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

# Выполнение запроса на создание покемона
response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.text)

# Проверка успешности запроса и извлечение pokemon_id
if response_create.status_code == 201:  # Убедитесь, что статус 201 (создано)
    created_pokemon = response_create.json()  # Предполагается, что ответ в формате JSON
    pokemon_id = created_pokemon.get('id')  # Измените 'id' на правильный ключ из вашего ответа

    # Обновление данных для смены имени и добавления покебола
    body_switch_name = {
        "pokemon_id": pokemon_id,
        "name": "generate",
        "photo_id": -1
    }

    body_add_pokeball = {
        "pokemon_id": pokemon_id
    }

    # Выполнение запроса на смену имени покемона
    response_switch_name = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_switch_name)
    print(response_switch_name.text)

    # Выполнение запроса на добавление покебола
    response_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_pokeball)
    print(response_add_pokeball.text)