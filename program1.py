n = int(input("enter the number of rows:"))
for i in range(n):
    for j in range(n-i+1):
        print(" ", end="")
    for j in range(i+1):
        print("*", end=" ")
    print()
    #inverted traingle
for i in range(n,0,-1):
    for j in range(n-i+2):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()