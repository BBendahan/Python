import requests

file_path = 'pokedex.csv'
url = 'https://pokeapi.co/api/v2/pokemon/'

def get_pokemon(name):
    url2 = f'{url}{name}'
    pokemon = requests.get(url2)

    if pokemon.status_code == 200:
        pokemon_data = pokemon.json()
        return pokemon_data
    if pokemon.status_code == 404:
        print('no se ha encontrado ese pokemon')
    return
    print('unexpected error')
    

with open (file_path, 'x') as file:
   
    for num in range(10000):

        pikachu = get_pokemon(num)

        if pikachu:
            file.write(f'{pikachu['name']}, {pikachu['id']}, {pikachu['height']}cm, {pikachu['weight']}kg\n')
#            print(f'{pikachu['name']}, {pikachu['id']}, {pikachu['height']}cm, {pikachu['weight']}kg')


