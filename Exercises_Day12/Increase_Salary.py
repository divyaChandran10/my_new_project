def inc_salary():
    print('Enter employee salary')
    emp_salary = float(input())
    if emp_salary > 0 and emp_salary <= 400.00:
        salary_inc = float(emp_salary * (15/100))
        new_salary = format(emp_salary + salary_inc, ".2f")
        format(salary_inc, ".2f")
        print(f'New salary: {new_salary} Increase: {salary_inc} Readjustment Rate: 15%')
    elif emp_salary >= 400.01 and emp_salary <= 800.00:
        salary_inc = float(format(float(emp_salary * (12/100)), ".2f"))
        new_salary = format(emp_salary + salary_inc, ".2f")
        print(f'New salary: {new_salary} Increase: {salary_inc} Readjustment Rate: 12%')
    elif emp_salary >= 800.01 and emp_salary <= 1200.00:
        salary_inc = float(format(float(emp_salary * (10/100)), ".2f"))
        new_salary = format(emp_salary + salary_inc, ".2f")
        print(f'New salary: {new_salary} Increase: {salary_inc} Readjustment Rate: 10%')
    elif emp_salary >= 1200.01 and emp_salary <= 2000.00:
        salary_inc = float(format(float(emp_salary * (7/100)), ".2f"))
        new_salary = format(emp_salary + salary_inc, ".2f")
        print(f'New salary: {new_salary} Increase: {salary_inc} Readjustment Rate: 7%')
    elif emp_salary > 2000:
        salary_inc = float(format(float(emp_salary * (4/100)), ".2f"))
        new_salary = format(emp_salary + salary_inc, ".2f")
        print(f'New salary: {new_salary} Increase: {salary_inc} Readjustment Rate: 4%')


if __name__ == '__main__':
    inc_salary()
