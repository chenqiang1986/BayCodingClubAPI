import requests


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

def main():
    search_term = input("Enter the name or the ID of a Pokemon: ")
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{search_term}")

    #print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        print_useful_info(data)
    else:
        print("Error Fetching Pokemon with Error Code: ", response.status_code)
        if (response.status_code == 404):
            print(f"Pokemon {search_term} not found. Please check the name or ID and try again.")

if __name__ == "__main__":    
    main()