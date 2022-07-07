import application.salary as sal
import application.db.people as pers
import datetime as d


def main(number):
    print(f'{sal.person_salary(pers.find_person(number))} время запроса {d.datetime.now()}')
    pass


if __name__ == '__main__':
    main(1)
