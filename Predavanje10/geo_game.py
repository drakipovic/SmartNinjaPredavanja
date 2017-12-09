from random import randint

capital_cities = {
    'Croatia': 'Zagreb',
    'United Kingdom': 'London',
    'Ireland': 'Dublin',
    'France': 'Paris',
    'Spain': 'Madrid',
    'Sweden': 'Stockholm',
    'Hungary': 'Budapest'
}

countries = capital_cities.keys()


def check_user_guess_correct(user_guess, country_name):
    if user_guess == capital_cities[country_name]:
        return True
    else:
        return False


if __name__ == '__main__':
    while True:

        which_country = randint(0, len(countries)-1)
        country_name = countries[which_country]

        print "> Game: What is the capital city of " + country_name + "?"
        user_guess = raw_input("User: ")

        if check_user_guess_correct(user_guess, country_name):
            print "> Game: This is correct!"
        else:
            print "> Game: Answer is not correct! Right answer is: " + capital_cities[country_name]

        want_more = raw_input("Do you want to guess some more? [yes/no]")

        if want_more == "no":
            break