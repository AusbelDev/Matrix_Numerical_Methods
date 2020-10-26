import math
from scipy.optimize import fmin
import numpy as np
from math import pi
def min_maxF(f,a,b):
    arr = []
    while(a<b):
        val = f(a)
        
        arr.append(val)
        a = a + 0.1

    return min(arr), max(arr)


def newtraph(f, d,xi,N):
    
    x_i = xi
    
    for n in range(1,N+1):
        if d(x_i) == 0:
            x_2 = x_i - (f(x_i)/(1))
        else:
            x_2 = x_i - (f(x_i)/d(x_i))
        if x_2 == 0:
            e = 0
        else:
            e = abs((x_2 - x_i)/x_2) * 100 

        f_m_n = f(x_2)

        print("Iteración #: ", n)
        print("Valor = ", x_2)
        print("Error = ", e, "\n")
        
        x_i = x_2
        
        if f_m_n == 0:
            print("Solución exacta encontrada")
            return x_2, e

           
    return x_2, e

def newtMejorado(f, d, s,xi,N):
    
    x_i = xi
    
    for n in range(1,N+1):
        x_2 = x_i - (f(x_i)*d(x_i)/(pow(d(x_i),2) - f(x_i)*s(x_i)))

        if x_2 == 0:
            e = 0
        else:
            e = abs((x_2 - x_i)/x_2) * 100 

        f_m_n = f(x_2)
        
        x_i = x_2
        
        if f_m_n == 0:
            print("Solución exacta encontrada")
            return x_2,e

           
    return x_2, e

i = 0
j = 0
h = 0
ch = 0
xi = 0.0
n = 14
b = []
f = lambda x: 0.16*x**3 -5*x+1
d = lambda x: 3*0.16*x**2 - 5
#s = lambda x: 600/(x**3) + 8*pi

val, e = newtraph(f,d,xi,n)
print("Newton-Raphson: ", val)
print("Error: ", e)

print("Función original evaluada en la raíz = ",f(2.2853))

""" while(i < 10):

    val, e = newtraph(f,d,xi,n)
    val2, e2 = newtMejorado(f,d,s,xi,n)
    b.append(val2)
    print("Newton-Raphson: ", val)
    print("Error: ", e)

    print("Newton mejorado: ", val2)
    print("Error: ", e2)
    if ch == val2:
        i+=1
    ch = val2
    xi = xi +1

minimo, maximo = min_maxF(f,min(b),max(b))

print("minimo de la funcion = ", minimo)
print("maximo de la funcion = ", maximo)

while(True):
    h = f(j)

    if h == maximo:
        print("El valor de x en el que la funcion es maxima es: ", j)
        break
    else:
        j = j+0.1 """
