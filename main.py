# Airport Management System

a = []
limit = 500


def num(msg):
    while True:
        try:
            n = int(input(msg))

            if n >= 0:
                return n
            else:
                print("Enter a positive number")

        except:
            print("Enter a valid number")


def add():

    if len(a) >= limit:
        print("No more flights can be added")
        return

    f = {}

    f["no"] = input("Enter flight number: ")

    # checking duplicate flight number
    for x in a:
        if x["no"] == f["no"]:
            print("Flight already exists")
            return

    f["from"] = input("Enter source city: ")
    f["to"] = input("Enter destination city: ")
    f["stop"] = input("Enter stoppage city (none if no stop): ")
    f["arrival"] = input("Enter arrival time: ")
    f["departure"] = input("Enter departure time: ")

    f["fuel"] = num("Enter fuel in liters: ")
    f["passengers"] = num("Enter number of passengers: ")
    f["crew"] = num("Enter number of crew members: ")

    a.append(f)

    print("Flight added successfully")


def show(f):

    print("--------------------------")
    print("Flight number :", f["no"])
    print("From          :", f["from"])
    print("To            :", f["to"])
    print("Stoppage      :", f["stop"])
    print("Arrival       :", f["arrival"])
    print("Departure     :", f["departure"])
    print("Fuel          :", f["fuel"], "liters")
    print("Passengers    :", f["passengers"])
    print("Crew          :", f["crew"])
    print("--------------------------")


def showall():

    if len(a) == 0:
        print("No flights available")
        return

    for f in a:
        show(f)

    print("Total flights:", len(a))


def search():

    n = input("Enter flight number: ")

    for f in a:

        if f["no"] == n:
            show(f)
            return

    print("Flight not found")


def delete():

    n = input("Enter flight number to delete: ")

    for f in a:

        if f["no"] == n:
            a.remove(f)
            print("Flight deleted")
            return

    print("Flight not found")


while True:

    print()
    print("***** AIRPORT MANAGEMENT *****")
    print("1. Add flight")
    print("2. Show all flights")
    print("3. Search flight")
    print("4. Delete flight")
    print("5. Exit")

    c = input("Enter your choice: ")

    if c == "1":
        add()

    elif c == "2":
        showall()

    elif c == "3":
        search()

    elif c == "4":
        delete()

    elif c == "5":
        print("Thank you")
        break

    else:
        print("Wrong choice")
