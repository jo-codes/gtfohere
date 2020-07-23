import json, random

with open("world_cities.json") as json_file:
    world = json.load(json_file)

random_city = random.choice(world)

print(f"{random_city['name']}, {random_city['country']}")

