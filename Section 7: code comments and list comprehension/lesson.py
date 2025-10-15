# List of names to be capitalized
names = ['john smith', 'jay santi', 'eva kuki']
# Use list comprehension to capitalize all names
capitalized_names = [name.title() for name in names]
# Print the updated list
print(capitalized_names)

usernames = ["john 1990", "alberta1970", "magnola2000"]
sizes = [len(username) for username in usernames]
print(sizes)

user_entries = ['10', '19.1', '20']
numbers = [float(entry) for entry in user_entries]
print(numbers)

numbers = [10, 20, 30]
print([number * 2 for number in numbers])


user_entries = ['10', '19.1', '20']
sum=0
for entry in user_entries:
    sum += float(entry)
print(sum)

numbers = [1,2,3,4,5]
squared_numbers = [number ** 2 for number in numbers]


# while True:
#     case = input("add, show, edit, complete or exit: ")
#     match case:
#         case "add":
#             item = input("Enter a todo item: ") + "\n"
#             file = open(r"todos.txt", "a")
#             file.writelines(item)
#             file.close()
#         case "show":
#             file = open(r"todos.txt", "r")
#             todos = file.readlines()
#             file.close()
#             for index, item in enumerate(todos):
#                 item = item.title().strip()
#                 print(f"{index + 1}. {item.capitalize()}\n", end="")
#         case "edit":
#             file = open(r"todos.txt", "r")
#             todos = file.readlines()
#             file.close()
#             number = int(input("Number of the item to edit: "))
#             if 0 < number <= len(todos):
#                 new_item = input("Enter the new todo item: ") + "\n"
#                 todos[number - 1] = new_item
#             else:
#                 print("Invalid item number.")
#             file = open(r"todos.txt", "w")
#             file.writelines(todos)
#             file.close()
#         case "complete":
#             number = int(input("Number of the item to complete: "))
#             if number <= 0 or number > len(todos):
#                 print("Invalid item number.")
#                 continue
#             else:
#                 print(f"Todo item {number} completed.")
#                 file = open(r"todos.txt", "r")
#                 todos = file.readlines()
#                 todos.pop(number - 1)
#                 file = open(r"todos.txt", "w")
#                 file.writelines(todos)
#                 file.close()
#         case "exit":
#             break
#         case _:
#             print("Unknown command.")
