users_list1 = [
    [111, 'Div'],
    [222, 'Mon']
]

users_list2 = [
    {'name': 'john', 'city': 'Berlin'},
    {'name': 'jack', 'city': 'Frankfurt'}
]

user1 = {'name': 'john', 'city': 'Berlin'}

for i in range(len(users_list2)):
    print(users_list2[i]['name'])

for key, value in user1.items():
    print(f'{key} = {value}')

print(users_list1[1])
print(users_list1[1][1])

print(users_list2[0])
print(users_list2[0]['city'])

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

numbers = dict(zip(keys, values))
print(numbers)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Sixty': 60, 'Forty': 40, 'Fifty': 50}

dict3 = dict(**dict1, **dict2)
dict4 = {**dict1, **dict2}
print(dict3)
print(dict4)

for 'Ten' in **key


