def rectangle(rows):
    print()
    print("1. Reactangle ")
    for i in range(rows):
        for j in range(rows):
            print("* ", end=" ")
        print()

def leftRightTriangle(rows):
    print()
    print("2. Left Right-Angled Triangle ")
    for i in range(rows):
        for j in range(i+1):
            print("* ", end=" ")
        print()

def leftDownwardRightTriangle(rows):
    print()
    print("3. Left Downward Right-Angled Triangle ")
    for i in range(rows):
        for j in range(i, rows):
            print("* ", end=" ")
        print()

def rightRightTriangle(rows):
    print()
    print("4. Right Right-Angled Triangle ")
    for i in range(rows):
        for j in range(i, rows):
            print(" ", end=" ")
        for j in range(i+1):
            print("*", end=" ")
        print()

def upwardTriangle(rows):
    print()
    print("5. Upward Triangle ")
    for i in range(rows):
        for j in range(i, rows):
            print(" ", end=" ")
        for K in range(i + 1):
            print("*", end=" ")
        for l in range(i):
            print("*", end=" ")
        print()

def downwardTriangle(rows):
    print()
    print("6. Downward Triangle ")
    for i in range(rows):
        for j in range(i):
            print(" ", end=" ")
        for K in range(i, rows):
            print("*", end=" ")
        for l in range(i+1, rows):
            print("*", end=" ")
        print()

def leftFacedTriangle(rows):
    print()
    print("7. Left Faced Triangle ")
    for i in range(rows*2):
        if(i<=rows):
            for k in range(i):
                print("*", end=" ")
        else:
            for l in range(i, rows*2):
                print("*", end=" ")
        print()

def rightFacedTriangle(rows):
    print()
    print("8. Right Faced Triangle ")
    for i in range(rows*2):
        if(i<=rows):
            for k in range(i, rows):
                print(" ", end=" ")
            for l in range(i):
                print("*", end=" ")
        else:
            for m in range(i-rows):
                print(" ", end=" ")
            for n in range(i, rows*2):
                print("*", end=" ")
        print()

def diamond(rows):
    print()
    print("9. Diamond ")
    for i in range(rows*2):
        if(i<=rows):
            for k in range(i, rows):
                print(" ", end=" ")
            for l in range(i):
                print("*", end=" ")
            for l in range(i-1):
                print("*", end=" ")
        else:
            for m in range(i-rows):
                print(" ", end=" ")
            for n in range(i, rows*2):
                print("*", end=" ")
            for n in range(i+1, rows*2):
                print("*", end=" ")
        print()

def diamondCover(rows):
    print()
    print("9. Diamond Cover")
    for i in range(rows*2):
        if(i<rows):
            for k in range(i, rows):
                print("*", end="")
            for l in range(i*2):
                print(" ", end="")
            for k in range(i, rows):
                print("*", end="")
        else:
            for m in range(i-rows+1):
                print("*", end="")
            for n in range(i+1, rows*2):
                print(" ", end=" ")
            for n in range(i-rows+1):
                print("*", end="")
        print()

if __name__ == '__main__':
    rows = 5 # int(input("Enter Numbers of Rows: "))
    rectangle(rows)
    leftRightTriangle(rows)
    leftDownwardRightTriangle(rows)
    rightRightTriangle(rows)
    upwardTriangle(rows)
    downwardTriangle(rows)
    leftFacedTriangle(rows)
    rightFacedTriangle(rows)
    diamond(rows)
    diamondCover(rows)
