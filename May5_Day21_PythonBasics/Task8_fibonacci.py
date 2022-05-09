def fibonacci(num1, num2, n):
    print('The Fibonacci series is ', num1, num2, end=' ')
    for i in range(2, n):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        i += 1
        print(num3, end=' ')


if __name__ == '__main__':
    num1 = 0
    num2 = 1
    number = int(input('Enter the number of sequence'))
    fibonacci(num1, num2, number)
