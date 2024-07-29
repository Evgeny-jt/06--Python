from application.db.people import *
from application.salary import *

if __name__ == '__main__':
    print('вызываю функцию calculate_salary из dirty_main.py')
    calculate_salary()
    print('вызываю функцию get_employees из dirty_main.py')
    get_employees()
