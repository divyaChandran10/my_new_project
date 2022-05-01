#from datetime import datetime
import calendar


def month_int(x):
    #now = datetime.now()
    for i in range(1, 13):
        if 0 < x <= 12:
            m = str(calendar.month_name[x]).capitalize()
            print(f'The month {x} is {m}')
            break
        else:
            print('Invalid month')
            break


if __name__ == '__main__':
    print('enter any month in integer')
    n = int(input())
    month_int(n)
