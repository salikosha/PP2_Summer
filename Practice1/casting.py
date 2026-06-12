from math import *
import numpy as np
import matplotlib.pyplot as plt
a=3
b=5
n=10
h=(b-a)/n
k=3

y=np.zeros(n)
y1=np.zeros(n-1)
s=np.zeros(n-1)
d=np.zeros(n-1)

def f(x): return exp(-sin(x/3))

for i in range(n):
    x=a+i*h
    y[i]=f(x)

for i in range(n-1):
    x=a+i*h+h/k
    y1[i]=f(x)
    s[i]=y[i]+(y[i+1]-y[i])/k
    d[i]=abs(y1[i]-s[i])

Ma=0
Sig=0
for i in range(n-1):
    Ma=Ma+d[i]/n
    Sig=Sig+sqrt(d[i]-Ma)/(n-1)

Sig=sqrt(Sig)
print(f'Sig:{Sig}')
print(f'Ma:{Ma}')
print(f's:{s}')
print(f'd:{d}')

x=np.linspace(a,b,n)
x1=np.linspace(a,b,n-1)

plt.plot(x,y,color="red",linestyle='-.',label="y")
plt.plot(x1,y1,color="blue",linestyle='-',label="y1")
plt.legend()
plt.show()