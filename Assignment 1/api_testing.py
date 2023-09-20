import requests

def get_pokedex_info(name_or_id):
    url = "https://pokeapi.co/api/v2/pokemon/{}/".format(name_or_id)
    response = requests.get(url)

    if response.status_code == 200:
        region_data = response.json()
        return region_data
    else:
        print(f"Error accessing API. Status code: {response.status_code}")
        return None

def ability_data(name_or_id):
    url = "https://pokeapi.co/api/v2/ability/{}/".format(name_or_id)

    response = requests.get(url)

    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()
        names = [item["name"] for item in data["names"]]
        sorted_names = sorted(names)
        return sorted_names

def sort_pokemon_names():
    url = "https://pokeapi.co/api/v2/pokemon-species/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        names = [item["name"] for item in data["results"]]
        sorted_names = sorted(names)
        return sorted_names
    else:
        print(f"Error accessing API. Status code: {response.status_code}")
        return None

def sort_move_names():
    url = "https://pokeapi.co/api/v2/move/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        names = [item["name"] for item in data["results"]]
        sorted_names = sorted(names)
        return sorted_names
    else:
        print(f"Error accessing API. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    sorted_ability_names = ability_data("stench")

    if sorted_ability_names is not None:
        print("Sorted Ability Names:")
        print(sorted_ability_names)
    else:
        print("Failed to fetch ability data.")

    sorted_pokemon_names = sort_pokemon_names()

    if sorted_pokemon_names is not None:
        print("\nSorted Pokemon Names:")
        print(sorted_pokemon_names)
    else:
        print("Failed to fetch Pokemon data.")

    sorted_move_names = sort_move_names()

    if sorted_move_names is not None:
        print("\nSorted Move Names:")
        print(sorted_move_names)
    else:
        print("Failed to fetch move data.")
