import requests
import json
from random import randint
from array import array
from webbrowser import get
from flask import Flask, render_template

url = 'https://pokeapi.co/api/v2/pokemon/'

app = Flask(__name__)
@app.route('/')
def main():
    names = []
    photos = []
    numberPokemon = []
    type = []
    weight = []
    high = []

    for i in range(0,6):
        result = randint(1, 800)
        pokemonName = str(result)
        numberPokemon.append(result)
        pokemon_data_url = url + pokemonName
        data = get_pokemon_data(pokemon_data_url)

        res = json.loads(requests.get(pokemon_data_url).text)
        image = res['sprites']
        image = image['front_default']
        photos.append(image)

        name_pokemon = data.get("name")
        names.append(name_pokemon)

        typePokemon = [types['type']['name'] for types in data['types']]
        type.append(", ".join(typePokemon))

        weightPokemon = data.get("weight")
        weight.append(weightPokemon)

        highPokemon = data.get("height")
        high.append(highPokemon)

    return render_template('index.html', len = len(names),  pokemon=names,
    imagen=photos, no=numberPokemon, tipo = type, peso=weight, altura=high)

def get_pokemon_data(urlPokemon =''):
    pokemonData = {
        "name": '',
        "height": '',
        "types": '',
        "weight": ''
    }

    response = requests.get(urlPokemon)
    data = response.json()

    pokemonData['name'] = data['name']
    pokemonData['height'] = data['height']
    pokemonData['types'] = data['types']
    pokemonData['weight'] = data['weight']

    return pokemonData
    

if __name__ == '__main__':
    app.run(debug=True)
