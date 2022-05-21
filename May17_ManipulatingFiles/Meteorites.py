import json


def file_load():
    with open('nasa.json', 'r') as file:
        data = list(json.load(file))
    return data


def get_mass():
    data = file_load()
    mass_value = 0
    for item in data:
        if 'mass' in item.keys():
            if item['fall'] == 'Fell':
                mass_value += float(item['mass'])
    print(f'The total weight of meteorites that fell is {mass_value}')

    count = 0
    for item in data:
        if item['fall'] == 'Fell':
            count = count + 1
    print(f'The number of meteorites that fell is {count}')


def get_massive():
    data = file_load()
    count = 0
    result = []
    for item in data:
        if 'mass' in item.keys():
            result.append(item)
            count = count + 1
    print('The number of items that weighs is:', count)
    massive = []
    for item in result:
        massive.append(float(item['mass']) / 1000)
    print(max(massive))
    for item in result:
        if float(item['mass']) / 1000 == max(massive):
            print(item['name'], item['fall'], item['mass'], item['year'])


if __name__ == '__main__':
    get_mass()
    get_massive()
