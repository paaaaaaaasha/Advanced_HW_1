from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime


print(datetime.now().replace(microsecond=0))

if __name__ == '__main__':

    get_employees()
    calculate_salary()
    # print(datetime.now().replace(microsecond=0))