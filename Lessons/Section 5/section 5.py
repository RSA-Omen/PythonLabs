#todo = []
todo = ["gym", "study", "code", "sleep"]

while True:
    case = input("add, show, edit, complete or exit: ")
    match case:
        case "add":
            item = input("Enter a todo item: ") + "\n"
            todo.append(item)    
        case "show":
            for index, item in enumerate(todo):
                item = item.title()
                print(f"{index + 1}. {item.capitalize()}\nshow", end="")
        case "edit":
            number = int(input("Number of the item to edit: "))
            if 0 < number <= len(todo):
                new_item = input("Enter the new todo item: ") + "\n"
                todo[number - 1] = new_item
            else:
                print("Invalid item number.")
        case "complete":
            number = int(input("Number of the item to complete: "))
            if 0 < number <= len(todo):
                todo.pop(number - 1)
            else:
                print("Invalid item number.")
        case "exit":
            break
        case _:
            print("Unknown command.")                      
    