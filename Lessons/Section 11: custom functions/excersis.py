# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     return_string = f"Max: {max(grades)}, Min: {min(grades)}"
#     return return_string
#
# print(get_max())


# def format_filename():
#     filename ="report.txt"
#     filename=filename[:-4]
#     filename = filename.capitalize()
#     return filename
#
# print(format_filename())

def square_number():
    number=5
    result=number**2
    return result

print(square_number())

def printgreeting(name):
    print(f"Hello {name}")
    
printgreeting("Lauchlan")

add_numbers = lambda num1, num2: num1 + num2

print(add_numbers(5, 10))

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(4))

print(even_or_odd(15))