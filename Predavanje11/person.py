from datetime import datetime

class Person(object):

    def __init__(self, first_name, last_name, gender, phone_number, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone_number = phone_number
        self.birth_year = birth_year

    def __str__(self):
        return '(' + self.first_name + ', ' + self.last_name + ', ' + self.gender + ', ' + self.phone_number + ', ' + str(self.birth_year) + ')'

    def full_name(self):
        return self.first_name + " " + self.last_name

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year



person_1 = Person(first_name='dino', last_name='rakipovic', gender='M', phone_number='0917848750', birth_year=1993)
person_2 = Person(first_name='josip', last_name='golub', gender='M', phone_number='8129371823', birth_year=1991)

print person_1

persons = [person_1, person_2]

for person in persons:
    print person

print person_1.get_age()