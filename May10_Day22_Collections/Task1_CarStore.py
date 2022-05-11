# The HR Department of the “Super Car Store” decided to create a file containing information about its employees. The
# intention is to create some programs that can extract some useful information from the dataset. The data you can
# find in the file employees.py as a list of dictionaries.
#
# After gathering the data they gave you the task of implementing some functions to extract the information,
# so you have to implement the following functions.
#
#     get_employee_by_name(name)
#     get_total_expenses()
#     get_employees_by_age(age)
#     get_average_age()
#     get_salary_by_name(name)
#
# For checking by name use the function/method of string variables called find it will return the position in the
# string where the first occurrence of the word appears or -1 if nothing is found. E.g.
#
# x = "some text to be used as example"
# x.find("example")
# 24
# x.find("not present")
# -1
#

from employees import employees


def get_employee_by_name(name):
    for employee in employees:
        index = (employee["employee_name"]).find(name)
        if index >= 0:
            print(employee)
            #break
    else:
        print('Employee not found')


def get_employees_by_age(age):
    for employee in employees:
        if employee["employee_age"] == age:
            print(employee)
    else:
        print('Employee not found at the specified age')


def get_salary_by_name(name):
    for employee in employees:
        index = (employee["employee_name"]).find(name)
        if index >= 0:
            print(f'Salary of {name} is {employee["employee_salary"]}')


def get_average_age():
    age = 0
    for employee in employees:
        age = age + employee["employee_age"]
    print(f'The average age of the employee is {int(age / (len(employees)))}')


def get_total_expenses():
    total_expenses = 0
    for employee in employees:
        total_expenses = total_expenses + employee["employee_salary"]
    print(f'The total expenses of the store is {total_expenses}')


if __name__ == '__main__':
    emp_name = input('Enter employee name')
    get_employee_by_name(emp_name)
    emp_age = int(input('Enter employee age'))
    get_employees_by_age(emp_age)
    get_salary_by_name(emp_name)
    get_average_age()
    get_total_expenses()
