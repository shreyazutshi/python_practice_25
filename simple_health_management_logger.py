def getdate():
    import datetime
    return datetime.datetime.now()

def log(k):
    print("Inside log function")
    c = input("Choose the data to log - Exercise or Food: ").strip().lower()

    if c == "exercise":
        value = input("Enter the exercise done: ")
        filename = f"{k.lower()}_ex.txt"
    elif c == "food":
        value = input("Enter the food eaten: ")
        filename = f"{k.lower()}_food.txt"
    else:
        print("Invalid log type. Please choose 'Exercise' or 'Food'.")
        return

    try:
        with open(filename, "a") as f:
            f.write(str(getdate()) + " : " + value + "\n")
        print("Data has been logged!")
    except Exception as e:
        print("Error logging data:", e)

def retrieve(k):
    print("Inside retrieve function")
    c = input("Choose the data to retrieve - Exercise or Food: ").strip().lower()

    if c == "exercise":
        filename = f"{k.lower()}_ex.txt"
    elif c == "food":
        filename = f"{k.lower()}_food.txt"
    else:
        print("Invalid retrieve type. Please choose 'Exercise' or 'Food'.")
        return

    try:
        with open(filename, "r") as f:
            print(f"\n{k}'s {c.capitalize()} Records:")
            print(f.read())
    except FileNotFoundError:
        print("No records found yet.")
    except Exception as e:
        print("Error retrieving data:", e)

print("Hospital Management Records:")
a = input("Choose the work today - log or retrieve: ").strip().lower()

if a == "log":
    b = input("Choose the patient name - Harry, Rohan, Hammad: ").strip().capitalize()
    if b in ["Harry", "Rohan", "Hammad"]:
        log(b)
    else:
        print("Invalid patient name.")
elif a == "retrieve":
    b = input("Choose the patient name - Harry, Rohan, Hammad: ").strip().capitalize()
    if b in ["Harry", "Rohan", "Hammad"]:
        retrieve(b)
    else:
        print("Invalid patient name.")
else:
    print("Invalid task selected. Please choose 'log' or 'retrieve'.")


