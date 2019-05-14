import matplotlib.pyplot as plt
import numpy as np
import random


n=int(input("Add meg a sorok számát: "))
m=int(input("Adj meg ennél egy kisebb számot: "))
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
    print()


plt.plot([1,2,3,4], [1,4,9,16], 'go')
plt.axis([0, 5, 0, 10])
plt.show()
