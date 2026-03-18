from typing import NamedTuple

class Asteroid(NamedTuple):
    diameter: float
    speed: float
    name: str

# This is my debug input, replace it with your code to load from response
asteroids = {
    "2020-1-1": [{
        "name": "my_asteroid",
        "estimated_diameter": {
            "kilometers": {
                "estimated_diameter_max": 1
            }
        },
        "close_approach_data": [
            {
                "relative_velocity": {
                    "kilometers_per_hour": 5
                }
            }
        ]
    },
    {
        "name": "your_asteroid",
        "estimated_diameter": {
            "kilometers": {
                "estimated_diameter_max": 2
            }
        },
        "close_approach_data": [
            {
                "relative_velocity": {
                    "kilometers_per_hour": 6
                }
            }
        ]
    }
    
    ]
}
# Debug input ends here.


largest_asteroid = Asteroid(diameter=0, speed=0, name="")
for date in asteroids:
    today = asteroids[date]

    for asteroid_json in today:
        asteroid = Asteroid(
            name = asteroid_json["name"],
            diameter = asteroid_json["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
            speed = asteroid_json["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"],
        )

        if asteroid.diameter > largest_asteroid.diameter:
            largest_asteroid = asteroid
            


print("largest asteroid from inputted date:", largest_asteroid.name)
print("diameter (km):", largest_asteroid.diameter)
print("speed (km/h):", largest_asteroid.speed)