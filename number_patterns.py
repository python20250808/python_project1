line = int(input("Wie viele Reihen? "))

def number_pattern1(line):
    for x in range(line):
        i = 0
        for _ in range(x + 1):
            i += 1
            print( i, end=" ")
        print("\n")
#number_pattern1(line)

def number_pattern2(line):
    for x in range(line):
        i = 0
        for _ in range(line - x):
            print(" ", end="")
        for _ in range(x):
                i += 1
                print(i, end=" ")
        print("\n")

#number_pattern2(line)

def number_pattern3(line):
    for x in range(line):
        i = 0
        for _ in range(line - x):
            print(" ", end = " ")
        for _ in range(x + 1):
            i += 1
            print(i, end=" ")
        print("\n")
#number_pattern3(line)

def number_pattern4(line):
    for x in range(line, 0, -1):
        i = 0
        for _ in range(x):
                i += 1
                if x != 1:
                    print(i, end=" ")
        if x != 1:
            print("\n")
    for x in range(line):
        i = 0
        for _ in range(x + 1):
            i += 1
            print(i, end=" ")
        print("\n")
#number_pattern4(line)

def number_pattern5(line):
    for x in range(line, 0, -1):
        i = 0
        if x != 1:
            for _ in range(line - x + 1):
                print(" ", end="")
        for _ in range(x):
                i += 1
                if x != 1:
                    print(i, end=" ")
        if x != 1:
            print("\n")
    for x in range(line):
        i = 0
        for _ in range(line - x):
            print(" ", end="")
        for _ in range(x + 1):
            i += 1
            print(i, end=" ")
        print("\n")

#number_pattern5(line)

def number_pattern6(line):
    for x in range(line):
        i = 0
        if x < line - 1:
            for _ in range(x + 1):
                i += 1
                print(i, end=" ")
            print("\n")
    for x in range(line, 0, -1):
        i = 0
        for _ in range(x):
                i += 1
                print(i, end=" ")
        if x != 1:
            print("\n")

#number_pattern6(line)

def number_pattern7(line):
    for x in range(line, 0, -1):
        i = 0
        for _ in range(x):
            i += 1
            print( i, end=" ")
        print("\n")
#number_pattern7(line)

def number_pattern8(line):
    for x in range(line, 0, -1):
        i = 0
        for _ in range(line - x):
            print(" ", end="")
        for _ in range(x):
                i += 1
                print(i, end=" ")
        print("\n")

#number_pattern8(line)

def number_pattern9(line):
    for x in range(line, 0, -1):
        i = 0
        for _ in range(line - x):
            print(" ", end=" ")
        for _ in range(x):
                i += 1
                print(i, end=" ")
        print("\n")

#number_pattern9(line)

def number_pattern10(line):
    for x in range(line, 0, -1):
        i = 0
        for _ in range(line - x):
            if x != 1:
                print(" ", end=" ")
        for _ in range(x):
                i += 1
                if x != 1:
                    print(i, end=" ")
        if x != 1:
            print("\n")
    for x in range(line):
        i = 0
        for _ in range(line - x - 1):
            print(" ", end = " ")
        for _ in range(x + 1):
                i += 1
                print(i, end=" ")
        print("\n")

#number_pattern10(line)

def number_pattern11(line):
    for x in range(line):
        i = 0
        for _ in range(line - x):
            print(" ", end="")
        for _ in range(x):
                i += 1
                if x != line:
                    print(i, end=" ")
        if x != line:
            print("\n")
    for x in range(line, 0, -1):
        i = 0
        for _ in range(line - x):
            print(" ", end="")
        for _ in range(x):
                i += 1
                print(i, end=" ")
        print("\n")

#number_pattern11(line)

def number_pattern12(line):
    for x in range(line):
        i = 0
        for _ in range(line - x - 1):
            print(" ", end = " ")
        for _ in range(x + 1):
            i += 1
            print(i, end=" ")
        print("\n")
    for x in range(line, 0, -1):
        i = 0
        for _ in range(line - x):
            print(" ", end=" ")
        for _ in range(x):
                i += 1
                if x != line:
                    print(i, end=" ")
        if x != line:
            print("\n")


#number_pattern12(line)
