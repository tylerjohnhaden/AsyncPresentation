import time


# every leap year from year 0

def filter_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


# builds list at once, slow
list_of_leap_years = [y for y in range(2017) if filter_leap_year(y)]

# builds list on demand, fast
generator_of_leap_years = (y for y in range(2017) if filter_leap_year(y))

for leap_year in list_of_leap_years:
    print(leap_year)

for leap_year in generator_of_leap_years:
    print(leap_year)


# defining generator functions
def random_number_generator(n):
    print('here init')

    for i in range(n):
        print('here {}'.format(i))

        yield ((i + 1) * time.time()) % 1


gen_object = random_number_generator(3)
print(gen_object)
print('returned {}'.format(next(gen_object)))
print('returned {}'.format(next(gen_object)))
print('returned {}'.format(next(gen_object)))
print('returned {}'.format(next(gen_object)))
