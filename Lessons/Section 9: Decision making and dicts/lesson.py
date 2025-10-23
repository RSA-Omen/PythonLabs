while True:
    case = input("add, show, edit, complete or exit: ")
    
    if 'add' in case:
        item = case[4:].strip()  # Extract item after 'add'
        if not item:  # If no item provided, prompt for it
            item = input("Enter a todo item: ") + "\n"
        with open(r"../todos.txt", "a") as file:
            file.writelines(item)
    elif 'show' in case:
        with open(r"../todos.txt", "r") as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.title().strip()
            print(f"{index + 1}. {item.capitalize()}\n", end="")
    elif 'edit' in case:
        with open(r"../todos.txt", "r") as file:
            todos = file.readlines()
        number = int(case[5:].strip()) if len(case) > 4 else int(input("Number of the item to edit: "))
        if 0 < number <= len(todos):
            new_item = input("Enter the new todo item: ") + "\n"
            todos[number - 1] = new_item
        else:
            print("Invalid item number.")
        with open(r"../todos.txt", "w") as file:
            file.writelines(todos)
    elif 'complete' in case:
        number = int(case[9:].strip()) if len(case) > 8 else int(input("Number of the item to complete: "))
        if number <= 0 or number > len(todos):
            print("Invalid item number.")
            continue
        else:   
            print(f"Todo item {number} completed.")
            with open(r"../todos.txt", "r") as file:
                todos = file.readlines()
            todos.pop(number - 1)
            with open(r"../todos.txt", "w") as file:
                file.writelines(todos)
    elif 'exit' in case:
        print("Exiting the program.")
        break
    else:
        print("Unknown command.")  