from cars_small import cars


def get_car_by_name(name):
    result = []
    count = 0
    for car in cars:
        if ((car['Identification']['ID']).lower()).find(name.lower()) > -1:
            result.append(car)
            print(result, '\n')
            count = 1
    if count != 1:
        print(f'{name} is unavailable')
    # alternate way
    # for car in cars:
    #     if ((car['Identification']['ID']).lower()).find(name.lower()) > -1:
    #         print(car, '\n')
    #         count = 1
    # if count != 1:
    #     print(f'{name} is unavailable')


def get_car_by_number_of_gears(no_of_gears):
    result = []
    count = 0
    for car in cars:
        if car["Engine Information"]["Number of Forward Gears"] == no_of_gears:
            result.append(car)
            print(result, '\n')
            count = 1
    if count != 1:
        print(f'Cars with {no_of_gears} gear(s) is unavailable')


def get_car_by_manufacturer(manuf_name):
    result = []
    count = 0
    for car in cars:
        if ((car['Identification']['Make']).lower()).find(manuf_name.lower()) > -1:
            result.append(car)
            print(result, '\n')
            count = 1
    if count != 1:
        print(f'Cars manufactured by {manuf_name} is unavailable')


def get_car_by_year(manuf_year):
    result = []
    count = 0
    for car in cars:
        if car['Identification']['Year'] == manuf_year:
            result.append(car)
            print(result, '\n')
            count = 1
    if count != 1:
        print(f'Cars manufactured in {manuf_year} is unavailable')


def get_car_by_average_consumption(des_consumption):
    result = []
    count = 0
    for car in cars:
        average_consumption = (car['Fuel Information']['City mpg'] + car['Fuel Information']['Highway mpg']) / 2
        if des_consumption >= average_consumption:
            print(car, '\n')
            count = 1
    if count != 1:
        print(f'Cars with an average consumption {des_consumption} is unavailable')


if __name__ == '__main__':
    car_name = input('Enter the car name')
    get_car_by_name(car_name)
    number_of_gears = int(input('Enter the number of gears'))
    get_car_by_number_of_gears(number_of_gears)
    manufacturer = input('Enter the manufacturer')
    get_car_by_manufacturer(manufacturer)
    year = int(input('Enter the year'))
    get_car_by_year(year)
    desired_consumption = float(input('Enter the desired consumption'))
    get_car_by_average_consumption(desired_consumption)
