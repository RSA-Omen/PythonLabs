password = input("Enter your password: ")
if len(password) > 7:
    print("Great password there!")
elif len(password) == 7:
    print("Password is OK, but not too strong")
elif len(password) < 8:
    print("Your password is weak.")



day_temperatures = {"morning": (15.0, 12.0, 13.0), "noon": (15.0, 12.0, 13.0), "evening": (15.0, 12.0, 13.0)}

# Data structure examples for future reference:

# LIST - mutable (can be changed), ordered, uses square brackets []
my_list = [1, 2, 3, 4, 5]
my_list[0] = 10  # Can modify elements
my_list.append(6)  # Can add elements
print("List:", my_list)

# TUPLE - immutable (cannot be changed), ordered, uses parentheses ()
my_tuple = (1, 2, 3, 4, 5)
# my_tuple[0] = 10  # This would cause an error - tuples are immutable
print("Tuple:", my_tuple)

# DICTIONARY - mutable (can be changed), key-value pairs, uses curly braces {}
my_dict = {"name": "John", "age": 25, "city": "New York"}
my_dict["age"] = 26  # Can modify values
my_dict["country"] = "USA"  # Can add new key-value pairs
print("Dictionary:", my_dict)
print(my_dict["age"])  # Access value by key


# SET - mutable (can be changed), unordered, uses curly braces {}
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Can add elements
my_set.remove(2)  # Can remove elements
print("Set:", my_set)   


if x==1: 
    print(1) 
elif x!=1: 
    print("not 1")
else: 
    print("something else")