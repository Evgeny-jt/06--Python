from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    print('вызываю функцию calculate_salary из main')
    calculate_salary()
    print('вызываю функцию get_employees из main')
    get_employees()
