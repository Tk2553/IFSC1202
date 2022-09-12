print ("First Timestamp")
x= input ("Enter Hours :")
y= input ("Enter Minutes :")
z= input ("Enter Seconds :")
R= int(x)*int(3600)  # Function for X value to sec
T= int(y)*int(60)  #Function for Y value to sec
print ("Second Timestamp")
(q)= input ("Enter Hours :")
(u)= input ("Enter Minutes :")
(i)= input ("Enter Seconds :")
(R2)= int(q)*int(3600)     # Function for X2 value to sec
(T2)= int(u)*int(60)     #Function for Y2 value to sec
s=((int(R2)-int(R))+(int(T2)-int(T))+(int(i)-int(z)))
print (s)