from datetime import *
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    time = datetime.now(tz=None)
    argument = 'строка'
    argument1 = 'данные'
    print(time)
    calculate_salary(argument)
    get_employees (argument1)


