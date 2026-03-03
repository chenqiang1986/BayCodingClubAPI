from collections import defaultdict

import requests
import json


def print_useful_info(data):
    id = data["id"]
    name = data["name"]
    height = data["height"]
    weight = data["weight"]
    print(f"ID: {id}")
    print(f"Name: {name}")
    print(f"Height: {height}")
    print(f"Weight: {weight}")

    types = data["types"]
    type_names = [t["type"]["name"] for t in types]

    stats = data["stats"]
    hp = 0
    for stat in stats:
        if stat["stat"]["name"] == "hp":
            hp = stat["base_stat"]
            break
    
    attack = 0
    for stat in stats:
        if stat["stat"]["name"] == "attack":
            attack = stat["base_stat"]
            break
    
    defense = 0
    for stat in stats:       
        if stat["stat"]["name"] == "defense":
            defense = stat["base_stat"]
            break

    print(f"Types: {', '.join(type_names)}")
    print(f"HP: {hp}")
    print(f"Attack: {attack}")
    print(f"Defense: {defense}")

    img_url = data["sprites"]["front_default"]
    print(f"Image URL: {img_url}")

def print_modifier(modifier, modifier_type, preposition):
    print(f"{modifier_type} Modifier:")

    modifer_to_types = defaultdict(list)
    for target_type, value in modifier.items():
        if (value != 1.0):
            modifer_to_types[value].append(target_type)
    
    for modifier_value, types in modifer_to_types.items():
        print(f"  {modifier_value}x damage {preposition}: {', '.join(types)}")

def calculate_attacking_modifier(data):
    types = data["types"]
    type_names = [t["type"]["name"] for t in types]

    # attacking_modifier['grass'] == 4.0 means
    # This pokemon does 4x damage to grass type pokemon
    attacking_modifier = defaultdict(lambda: 1.0)

    for type_name in type_names:
        response = requests.get(f"https://pokeapi.co/api/v2/type/{type_name}")
        if response.status_code != 200:
            continue

        type_data = json.loads(response.content)
        double_damage_to = type_data["damage_relations"]["double_damage_to"]
        half_damage_to = type_data["damage_relations"]["half_damage_to"]
        no_damage_to = type_data["damage_relations"]["no_damage_to"]

        for target_type in double_damage_to:
            attacking_modifier[target_type["name"]] *= 2.0

        for target_type in half_damage_to:
            attacking_modifier[target_type["name"]] *= 0.5

        for target_type in no_damage_to:
            attacking_modifier[target_type["name"]] *= 0.0

    return attacking_modifier


def calculate_defense_modifier(data):
    types = data["types"]
    type_names = [t["type"]["name"] for t in types]

    # attacking_modifier['grass'] == 4.0 means
    # This pokemon does 4x damage to grass type pokemon
    defense_modifier = defaultdict(lambda: 1.0)

    for type_name in type_names:
        response = requests.get(f"https://pokeapi.co/api/v2/type/{type_name}")
        if response.status_code != 200:
            continue

        type_data = json.loads(response.content)
        double_damage_from = type_data["damage_relations"]["double_damage_from"]
        half_damage_from = type_data["damage_relations"]["half_damage_from"]
        no_damage_from = type_data["damage_relations"]["no_damage_from"]

        for target_type in double_damage_from:
            defense_modifier[target_type["name"]] *= 2.0

        for target_type in half_damage_from:
            defense_modifier[target_type["name"]] *= 0.5

        for target_type in no_damage_from:
            defense_modifier[target_type["name"]] *= 0.0

    return defense_modifier

def main():
    search_term = input("Enter the name or the ID of a Pokemon: ")
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{search_term}")

    #print(response.status_code)
    if response.status_code == 200:
        pokemon_data = json.loads(response.content)
        attacking_modifer = calculate_attacking_modifier(pokemon_data)
        defense_modifier = calculate_defense_modifier(pokemon_data)

        print_useful_info(pokemon_data)
        print_modifier(attacking_modifer, "Attacking", "to")
        print_modifier(defense_modifier, "Defense", "from")
    else:
        print("Error Fetching Pokemon with Error Code: ", response.status_code)
        if (response.status_code == 404):
            print(f"Pokemon {search_term} not found. Please check the name or ID and try again.")

if __name__ == "__main__":    
    main()