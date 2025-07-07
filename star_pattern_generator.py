try:
    n = int(input("Enter the number of rows you want to print: "))
    bool_val = int(input("Choose the pattern (1 for increasing, 0 for decreasing): "))

    if bool_val == 1:
        for i in range(1, n + 1):
            print("*" * i)
    elif bool_val == 0:
        for i in range(n, 0, -1):
            print("*" * i)
    else:
        print("Invalid choice! Please enter 0 or 1.")
except ValueError:
    print("Invalid input! Please enter numeric values only.")
