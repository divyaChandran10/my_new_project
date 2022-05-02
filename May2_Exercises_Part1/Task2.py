import datetime

date = datetime.datetime.now()


def is_weekend(date):
    if (datetime.datetime.weekday(date)) == 5 or (datetime.datetime.weekday(date)) == 6:
        return 'True'
    else:
        return 'False'


if __name__ == '__main__':
    #date = datetime.datetime.now()
    #print(date)
    #is_weekend(date)
    print(is_weekend(datetime.date(2021, 8, 6)))
    print(is_weekend(datetime.date(2021, 8, 7)))
    print(is_weekend(datetime.date(2021, 8, 8)))
    print(is_weekend(datetime.date(2021, 8, 9)))
