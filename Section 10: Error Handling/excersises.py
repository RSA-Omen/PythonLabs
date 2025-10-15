now_test = 1


if now_test == 1:
    try:
        total_value = float(input("Enter total value: "))
        value = float(input("Enter value: "))
        percentage = (value / total_value) * 100
        print(f"That is {percentage}%")
    except ValueError:
        print("You need to enter a number. Run the program again.")
    except ZeroDivisionError:
        print("The total value cannot be zero")


if now_test == 2:
    colors = [11, 34, 98, 43, 45, 54, 54]
    for color in colors:
        if color > 50:
            print(color)

passwords = ["acasd9983k", "34aiufaac99", "98jjanf", "afjj879"]

filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

for filename in filenames:
    print(filename.replace(".txt", "").capitalize())