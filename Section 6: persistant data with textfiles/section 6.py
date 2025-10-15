#todo = []

while True:
    case = input("add, show, edit, complete or exit: ")
    match case:
        case "add":
            item = input("Enter a todo item: ") + "\n"
            file = open(r"todos.txt", "a")
            file.writelines(item)
            file.close()
        case "show":
            file = open(r"todos.txt", "r")
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                item = item.title()
                print(f"{index + 1}. {item.capitalize()}\n", end="")
        case "edit":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()
            number = int(input("Number of the item to edit: "))
            if 0 < number <= len(todos):
                new_item = input("Enter the new todo item: ") + "\n"
                todos[number - 1] = new_item
            else:
                print("Invalid item number.")
            file = open(r"todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "complete":
            number = int(input("Number of the item to complete: "))
            if 0 < number <= len(todos):
                todos.pop(number - 1)
            else:
                print("Invalid item number.")
        case "exit":
            break
        case _:
            print("Unknown command.")