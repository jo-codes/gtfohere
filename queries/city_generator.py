import json, random

with open("../data/airports.json") as json_file:
    world = json.load(json_file)


def random_city():

    city = random.choice(world)

    return city


# print(f"{random_city()}\n\n")
