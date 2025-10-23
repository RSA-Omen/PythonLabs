





while True:
    case = input("add, show, edit, complete or exit: ")
    
    if case.startswith('add'):
        try:
            item = case[4:].strip()  # Extract item after 'add'
            if not item:  # If no item provided, prompt for it
                item = input("Enter a todo item: ")
            if not item.endswith('\n'):
                item += '\n'
            with open("/home/lauchlan/thelab/todos.txt", "a") as file:
                file.write(item)
            print(f"Added: {item.strip()}")
        except Exception as e:
            print(f"An error occurred while adding the item: {e}")
            continue
    
    elif case.startswith('show'):
        try:
            todos = get_todos()
            if not todos:
                print("No todos found. Please add an item first.")
                continue
            for i, todo in enumerate(todos, 1):
                print(f"{i}. {todo.strip()}")
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

    elif case.startswith('edit'):
        try:
            todos = get_todos()
            if not todos:
                print("No todos found. Please add an item first.")
                continue
            if len(case) > 4:
                number_str = case[5:].strip()
                number = int(number_str)
            else:
                number = int(input("Number of the item to edit: "))
            if 0 < number <= len(todos):
                new_item = input("Enter the new todo item: ")
                if not new_item.endswith('\n'):
                    new_item += '\n'
                todos[number - 1] = new_item
                with open("/home/lauchlan/thelab/todos.txt", "w") as file:
                    file.writelines(todos)
                print(f"Updated item {number}")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")       
            continue
        except Exception as e:
            print(f"An error occurred: {e}")    
            continue
        
      
    elif case.startswith('complete'):
        try:
            todos = get_todos()
            if not todos:
                print("No todos found. Please add an item first.")
                continue
            if len(case) > 8:
                number_str = case[9:].strip()
                number = int(number_str)
            else:
                number = int(input("Number of the item to complete: "))
            if 0 < number <= len(todos):
                completed_item = todos.pop(number - 1)
                with open("/home/lauchlan/thelab/todos.txt", "w") as file:
                    file.writelines(todos)
                print(f"Todo item '{completed_item.strip()}' completed.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
    elif case.startswith('exit'):
        exit("Exiting the program.")
    else:
        print("Unknown command.")  
