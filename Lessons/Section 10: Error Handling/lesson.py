while True:
    case = input("add, show, edit, complete or exit: ")
    
    if case.startswith('add'):
        try:
            with open(r"../todos.txt", "a") as file:
                item = case[4:].strip()  # Extract item after 'add'
                if not item:  # If no item provided, prompt for it
                    item = input("Enter a todo item: ") + "\n"
                file.writelines(item)
        except Exception as e:
            print(f"An error occurred while adding the item: {e}")
            continue
    
    elif case.startswith('show'):
        try:
            with open(r"../todos.txt", "r") as file:
                todos = file.readlines()
        except FileNotFoundError:
            print("The todo file does not exist. Please add an item first.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

    
    elif case.startswith('edit'):
        try:
            with open(r"../todos.txt", "r") as file:
                todos = file.readlines()
            if len(case) > 4:
                number_str = case[5:].strip()
                number = int(number_str)
            else:
                number = int(input("Number of the item to edit: "))
            if 0 < number <= len(todos):
                new_item = input("Enter the new todo item: ") + "\n"
                todos[number - 1] = new_item
            else:
                print("Invalid item number.")
            with open(r"../todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Please enter a valid number.")       
            continue
        except FileNotFoundError:
            print("The todo file does not exist. Please add an item first.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")    
            continue
        
        
    elif case.startswith('complete'):
        try:
            with open(r"../todos.txt", "r") as file:
                todos = file.readlines()
            if len(case) > 9:
                number_str = case[9:].strip()
                number = int(number_str)
            else:
                number = int(input("Number of the item to complete: "))
            if 0 < number <= len(todos):
                print(f"Todo item {number} completed.")
                todos.pop(number - 1)
                with open(r"../todos.txt", "w") as file:
                    file.writelines(todos)
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")
            continue
        except FileNotFoundError:
            print("The todo file does not exist. Please add an item first.")
            continue
        else:   
            print(f"Todo item {number} completed.")
            with open(r"../todos.txt", "r") as file:
                todos = file.readlines()
            todos.pop(number - 1)
            with open(r"../todos.txt", "w") as file:
                file.writelines(todos)
    elif case.startswith('exit'):
        exit("Exiting the program.")
    else:
        print("Unknown command.")  
