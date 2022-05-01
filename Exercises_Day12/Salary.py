def cal_salary():
    print('Enter employee number')
    emp_num = int(input())
    print('Enter hours worked')
    work_hours = int(input())
    print('Enter amount per hour')
    amt_per_hour = float(input())
   # emp_salary = format(float(work_hours * amt_per_hour), ".2f")
    emp_salary = float(work_hours * amt_per_hour)
    print("EMPLOYEE NUMBER = " + str(emp_num))
    print("Salary = U$ " + str(emp_salary))

    print(f'salary = U$ {emp_salary:.2f}')

if __name__ == '__main__':
    cal_salary()
