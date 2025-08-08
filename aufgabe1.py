line = int(input("Wie viele Striche? "))
def square_line(line):
    for _ in range(line):
        for _ in range(line):
            print("-", end=" ")
        print("\n")

#square_line(line)

def right_triangle(line):
    for x in range(line):
        for _ in range(x + 1):
            print("-", end=" ")
        print("\n")

#right_triangle(line)

def triangle(line):
    for x in range(line):
        for _ in range(line - x):
            print(" ", end="")
        for _ in range(2 * x + 1):
                print("-", end="")
        print("\n")

#triangle(line)