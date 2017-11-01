# every leap year from the dawn of time
import time


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
    # print(leap_year)
    pass

for leap_year in generator_of_leap_years:
    # print(leap_year)
    pass


# defining generator functions
def generate_random_numbers(n):
    print('here init')

    for i in range(n):
        print('here {}'.format(i))

        yield (i * 9) % 100


gen_object = generate_random_numbers(3)
print(gen_object)
print('returned {}'.format(next(gen_object)))
print('returned {}'.format(next(gen_object)))
print('returned {}'.format(next(gen_object)))
print('returned {}'.format(next(gen_object)))

