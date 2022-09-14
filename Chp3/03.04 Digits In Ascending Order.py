x=int(input("Enter a 3 digit number : "))
a=x//100
b=(x%100)//10
c=(x%100)%10
if a<b and b<c :
    print ("Yes")
else:
    print("No")