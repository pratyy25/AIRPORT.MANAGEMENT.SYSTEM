 Airport Management System
# simple project using list and dictionary

flights = []      
limit = 500       


def add():
    if len(flights) >= limit:
        print("No space, 500 flights are already stored")
        return

    f = {}
    f["no"] = input("Enter flight number: ")

    
    for x in flights:#
        if x["no"] == f["no"]:
            print("This flight is already added")
            return


    f["from"] = input("Enter source city: ")
    f["to"] = input("Enter destination city: ")
    f["stop"] = input("Enter stoppage city (write none if no stop): ")
    f["arrival"] = input("Enter arrival time: ")
    f["departure"] = input("Enter departure time: ")
    f["fuel"] = int(input("Enter refueling amount in liters: "))
    f["passengers"] = int(input("Enter number of passengers: "))
    f["crew"] = int(input("Enter number of crew members: "))

    flights.append(f)
    print("Flight added")


def show(f):
    print("-----------------------------")
    print("Flight number  :", f["no"])
    print("Route          :", f["from"], "to", f["to"])
    print("Stoppage       :", f["stop"])
    print("Arrival time   :", f["arrival"])
    print("Departure time :", f["departure"])
    print("Fuel filled    :", f["fuel"], "liters")
    print("Passengers     :", f["passengers"])
    print("Crew members   :", f["crew"])
    print("-----------------------------")


def show_all():
    if len(flights) == 0:
        print("No flights available")
    else:
        for f in flights:
            show(f)
        print("Total flights =", len(flights))


def search():
    n = input("Enter flight number to search: ")
    found = False
    for f in flights:
        if f["no"] == n:
            show(f)
            found = True
    if found == False:
        print("Flight not found")


def delete():
    n = input("Enter flight number to delete: ")
    for f in flights:
        if f["no"] == n:
            flights.remove(f)
            print("Flight deleted")
            return
    print("Flight not found")


# main program
while True:
    print("\n***** AIRPORT MANAGEMENT *****")
    print("1. Add flight")
    print("2. Show all flights")
    print("3. Search flight")
    print("4. Delete flight")
    print("5. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        add()
    elif ch == "2":
        show_all()
    elif ch == "3":
        search()
    elif ch == "4":
        delete()
    elif ch == "5":
        print("Thank you")
        break
    else:
        print("Wrong choice")
