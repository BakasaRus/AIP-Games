games = {
    1: {
        'name': 'Super Mario 3D World + Bowser\'s Fury',
        'price': 4499
    },
    2: {
        'name': 'Super Mario Odyssey',
        'price': 4499
    },
    3: {
        'name': 'The Legend Of Zelda: Breath of the Wild',
        'price': 5249
    },
    4: {
        'name': 'Astral Chain',
        'price': 4499
    },
    5: {
        'name': 'NBA 2K20',
        'price': 179,
        'sale': True
    },
}


def find_by_name(name: str):
    result = {}

    for index, game in games.items():
        if name.lower() in game['name'].lower():
            result[index] = game

    return result
