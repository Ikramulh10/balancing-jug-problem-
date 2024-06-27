# Initialize the jug and their capacity
# Water jug model using DFS model

def main():
    a = int(input("Enter Jug A Capacity: "))
    b = int(input("Enter Jug B Capacity: "))
    ai = int(input("Initially Water in Jug A: "))
    bi = int(input("Initially Water in Jug B: "))
    af = int(input("Final State of Jug A: "))
    bf = int(input("Final State of Jug B: "))

    # Print List Of Operations
    print("List Of Operations You can Do:")
    print("1. Fill Jug A Completely")
    print("2. Fill Jug B Completely")
    print("3. Empty Jug A Completely")
    print("4. Empty Jug B Completely")
    print("5. Pour From Jug A till Jug B filled Completely or A becomes empty")
    print("6. Pour From Jug B till Jug A filled Completely or B becomes empty")
    print("7. Pour all From Jug B to Jug A")
    # print("8. Pour all From Jug A to Jug B")

    # Loop
    while (ai != af or bi != bf):
        op = int(input("Enter the Operation: "))

        if op == 1:
            ai = a
        elif op == 2:
            bi = b
        elif op == 3:
            ai = 0
        elif op == 4:
            bi = 0
        elif op == 5:
            if b - bi > ai:
                bi = b + bi
                ai = 0
            else:
                ai = ai - (b - bi)
                bi = b
        elif op == 6:
            if a - ai > bi:
                ai = ai + bi
                bi = 0
            else:
                bi = bi - (a - ai)
                ai = a
        elif op == 7:
            ai = ai - (bi + b)
            bi = 0

        print(ai, bi)
        if op == 7:
            break

if __name__ == "__main__":
    main()
