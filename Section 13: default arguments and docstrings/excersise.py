"""

def get_age(year_of_birth,current_year=2025):
    return current_year - year_of_birth

print(get_age(1990))

def get_age(year_of_birth,current_year=2025):
    return current_year - year_of_birth

print(get_age(1990,2026))

def get_age(year_of_birth,current_year=2025):
    return current_year - year_of_birth



def get_nr_items(stringWithCommas="john,lisa, teresa"):
    return len(stringWithCommas.split(","))

print(get_nr_items())



def area_of_square(side_length=10):
    return side_length * side_length

print(area_of_square())
print(area_of_square(5))


def add_two_numbers(num1=5, num2=3):
    return num1 + num2
print(add_two_numbers())




def check_temperature(temperature=37):
    if temperature > 7:
        return "warm"
    else:
        return "cold"
print(check_temperature())
print(check_temperature(38))

"""


def password_length_checker(password="123456789"):
    if len(password) > 7:
        return True
    else:
        return False
print(password_length_checker())
print(password_length_checker("1234567890"))

"""
