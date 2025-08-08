todos = []

for _ in range(10000):
    print("Was willst du tun? ")
    print(" (1) To-dos anzeigen")
    print(" (2) To-dos hinzufügen")
    option = int(input("Bitte auswählen: "))
    if option == 1:
        for todo in todos:
            print(f" - {todo}")
    if option == 2:
        newitem = input("Was möchtest du hinzufügen? ")
        todos.append(newitem)
    print("")
    print("---------------")
    print("")

