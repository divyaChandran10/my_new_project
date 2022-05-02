import datetime

date = datetime.datetime.now()


def is_weekend(date):
    print(str(datetime.datetime.weekday(date)))
    if (datetime.datetime.weekday(date)) == 5 or (datetime.datetime.weekday(date)) == 6:
        print('True')
    else:
        print('False')


if __name__ == '__main__':
    date = datetime.datetime.now()
    print(date)
    is_weekend(date)
