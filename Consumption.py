def avg_consumption(d, f):
    avg = d / f
    print(f'{avg:.3f} km/l')


if __name__ == '__main__':
    print('Enter distance travelled')
    dist_travel = float(input())

    print('Enter fuel consumed')
    fuel_consumed = float(input())

    avg_consumption(dist_travel, fuel_consumed)
