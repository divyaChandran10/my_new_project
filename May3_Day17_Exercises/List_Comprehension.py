list = [{"value": 3}, {"value": 4}, {"value": 5}]
evens = []
odds = []

if __name__ == '__main__':
    evens = [i for i in list if i['value'] % 2 == 0]
    odds = [i for i in list if i['value'] % 2 != 0]

print(evens)
print(odds)
