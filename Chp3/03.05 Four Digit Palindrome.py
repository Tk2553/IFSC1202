x=int(input("Enter a Number: "))
z=x//1000
a=x//100%10
b=(x%100)//10
c=(x%100)%10
if z==c and a==b : 
    print("Yes")
else: 
    print("No")