x=float(input("Enter from Value : "))
u=str(input("Enter from Unit (in,ft,yd,mi) :\n "))
a=str(input("Enter to Unit(in,ft,yd,mi) :\n "))
if u == "ft" and a == "yd": 
    print(round(x*.33333333333333,7))
if u == "ft" and a == "in": 
    print(round(x*12,7))
if u == "ft" and a == "mi": 
    print(round(x/5280,7))
if u == "in" and a == "yd": 
    print(round(x*(1/36),7))
if u == "in" and a == "mi": 
    print(round(x/63360,7))
if u == "in" and a == "ft": 
    print(round(x/12,7))
if u == "yd" and a == "in": 
    print(round(x*36,7))
if u == "yd" and a == "ft": 
    print(round(x*3,7))
if u == "yd" and a == "mi": 
    print(round(x/1760,7))
if u == "mi" and a == "in": 
    print(round(x*63360,7))
if u == "mi" and a == "ft": 
    print(round(x*5280,7))
if u == "mi" and a == "yd": 
    print(round(x*1760,7))
if u == "ft" and a == "ft": 
    print(round(x*1,7))
if u == "yd" and a == "yd": 
    print(round(x*1,7))
if u == "in" and a == "in": 
    print(round(x*1,7))
if u == "mi" and a == "mi": 
    print(round(x*1,7))
if u!="in,ft,yd,mi" :
    print("Input is not Valid")