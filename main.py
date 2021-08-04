from matplotlib import pyplot as plt
import pandas as pd
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot
import numpy as np

x1_list = []
x2_list = []
x3_list = []
x4_list = []


def jacobi(A, b, e=0.1, x=None):
    if x is None:
        x = zeros(len(A[0]))

    D = diag(A)
    R = A - diagflat(D)

    count = 1
    condition = True
    x0 = array(x)

    print('\nCount\tx1\tx2\tx3\tx4\n')
    while condition:
        x = (b - dot(R,x)) / D
        print('%d\t%0.4f\t%0.4f\t%0.4f\t%0.4f\n' %(count, x[0],x[1],x[2],x[3]))
        
        x1_list.append(abs(4-x[0]))
        x2_list.append(abs(2-x[1]))
        x3_list.append(abs(-3-x[2]))
        x4_list.append(abs(6-x[3]))

        
        e1 = abs(x0[0]-x[0])
        e2 = abs(x0[1]-x[1])
        e3 = abs(x0[2]-x[2])
        e4 = abs(x0[3]-x[3])
        
        count+=1
        x0=array(x)
        condition = (e1 > e or e2 > e or e3 > e or e4 > e)
        
    return np.round(x,2)


A = array([[15.0,3.0, 5.0, -6.0],[4.0,-25.0, 2.0, 4.0],[2.0,-5.0, 20.0, 1.0],
[1.0,3.0, 6.0, -12.0]])
b = array([15.0,-16.0, -56, -80])

while True:
    try:
        print('Wprowadź punkty startowe: ')
        p1, p2, p3, p4 = [float(p) for p in input().split()]
        e = float(input('Podaj dokładność: '))
    except ValueError:
        print ('Stosuj się do zasad:/')
    else:
        guess = array([p1,p2,p3,p4])
        sol = jacobi(A,b,e,x=guess)
        break

print ("A:")
pprint(A)

print ("b:")
pprint(b)

print ("x:")
pprint(sol)
plt.plot(x1_list[5:])
plt.plot(x2_list[5:])
plt.plot(x3_list[5:])
plt.plot(x4_list[5:])


wszystkie = []
wszystkie.append(x1_list)
wszystkie.append(x2_list)
wszystkie.append(x3_list)
wszystkie.append(x4_list)


print("Różnica odległości między szua punktami x1,x2,x3,x4 a ich przybliżeniem")
