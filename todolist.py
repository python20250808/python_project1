todos = ["apfel", "banane", "birne"]

for _ in range(2):
    print("--------Aufgabe-------------")
    newitem = input("Was möchtest du hinzufügen? ")
    todos.append(newitem)
# bu program todos listelerini yazdirir, bilgine
    for todo in todos:
        print(f" - {todo}")
