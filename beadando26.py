from math import *
x=19293949596
a=10203040506
b=sqrt(a)
y=sqrt(x)

for i in range(int(b),int(y+1),1):
    z=i*i
    v=list(str(z))
    if v[0]=="1" and v[2]=="2" and v[4]=="3" and v[6]=="4" and v[8]=="5" and v[10]=="6":
        print(i)
