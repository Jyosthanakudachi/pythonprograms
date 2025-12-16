a = int(input("enter first no: "))
b = int(input("enter second no: "))
c = int(input("enter third no: "))

if(a >= b and a >= c):
    print("the fisrt no is largest" , a);
elif(b >= c):
    print("the second letter is largest", b)
else:
    print("third no is largest" , c)