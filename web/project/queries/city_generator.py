import json, random

with open("airports.json") as json_file:
    world = json.load(json_file)


def random_city():

    city = random.choice(world)

    return city


# print(random_city())
