if __name__ == '__main__':
    # Task 1
    city = 'London'
    print(city)

    # Task 2
    city = 'berlin'
    population = 3645000
    print(f'{city.capitalize()}: {population}')

    # Task 3
    city = 'london'
    population = 9000000
    if city.isalpha():
        print(f'City: {city.capitalize()} ({city.isalpha()}) \nPopulation: {population}')

    # Task 4
    text = """Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"""
    if text.find('capital'):
        capital = text.find('capital')
        print(f'capital: {capital}')

    # Task 5
    text = """Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"""
    list_text = text.split(' ')
    print(list_text)

    # Task 6
    text = """Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"""
    new_text = text.replace('capital', 'capital of Germany')
    print(new_text)

