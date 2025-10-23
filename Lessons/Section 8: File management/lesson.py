while True:
    case = input("add, show, edit, complete or exit: ")
    match case:
        case "add":
            item = input("Enter a todo item: ") + "\n"
            with open(r"todos.txt", "a") as file:
                file.writelines(item)
        case "show":
            with open(r"todos.txt", "r") as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                item = item.title().strip()
                print(f"{index + 1}. {item.capitalize()}\n", end="")
        case "edit":
            with open(r"todos.txt", "r") as file:
                todos = file.readlines()
            number = int(input("Number of the item to edit: "))
            if 0 < number <= len(todos):
                new_item = input("Enter the new todo item: ") + "\n"
                todos[number - 1] = new_item
            else:
                print("Invalid item number.")
            with open(r"todos.txt", "w") as file:
                file.writelines(todos)
        case "complete":
            number = int(input("Number of the item to complete: "))
            if number <= 0 or number > len(todos):
                print("Invalid item number.")
                continue
            else:
                print(f"Todo item {number} completed.")
                with open(r"todos.txt", "r") as file:
                    todos = file.readlines()
                todos.pop(number - 1)
                with open(r"todos.txt", "w") as file:
                    file.writelines(todos)
        case "exit":
            break
        case _:
            print("Unknown command.")



with open("file.txt", 'r') as file:
    print(file.read())
    print(len(file.read()))

try:
    with open(r"files/members.txt", "r") as file:
        members = file.readlines()
        print(members)
except FileNotFoundError:
    print("The file was not found.")
except IOError:
    print("An error occurred while reading the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}") 
finally:
    print("Execution completed.")   
