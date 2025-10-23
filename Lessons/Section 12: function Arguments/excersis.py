def strength(password):
    if len(password)>7 && any(char.isdigit() for char in password) && any(char.isupper() for char in password):
        return "Strong"
    else:
        return "Weak Password"
    

def get_average(list_numbers):
    return sum(list_numbers) / len(list_numbers) if list_numbers else 0


def greeting(person_name):
    return f"Hello {person_name}, welcome to the program!"

greeting = lambda person_name: f"Hello {person_name}, welcome to the program!"

def greeting(person_name):
    return f"Hi {person_name.capitalize()}"

def add(*args):
    return sum(args)

print(add(3, 5, 5))  # Outputs: 13