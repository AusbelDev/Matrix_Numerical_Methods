import matrix as mx
import matplotlib.pyplot as plt
import numpy as np
import csv
from pathlib import Path
import sympy
from sympy import *
import pandas as pd
import math
plt.style.use('ggplot')
""" x = np.array([2.,3.,4.,5.,6.])
y = np.array([2.,6.,5.,5.,6.]) """

def dataAcquisition(gui, path, number, row0,row1):
    if gui == 'user':
        print("Enter values or read a CSV file?")
        sel = input("Write 'file' to read the CSV file or enter 'manual' to manually enter the values: ")

        if sel == 'manual':
            
            number=input("Enter the number of data values: ")
            
            x=np.array([0 for i in range(0,int(number))])
            y=np.array([0 for i in range(0,int(number))])

            print("Enter the data points in x,y format\n")

            for i in range(0,int(number)):
                x[i] = float(input("x_" + str(i) + " :"))
                y[i] = float(input("y_" + str(i) + " :"))
                print("\n")

        elif sel == 'file':

            

            path = input("Enter the file path: ")
            number=input("Enter the number of data values: ")
            
            x=np.array([0 for i in range(0,int(number))])
            y=np.array([0 for i in range(0,int(number))])
            #filename = Path(path)
            with open(path,'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader) #skip header

                count=0
                sel=0
                for row in csv_reader:
                    #print(row)
                    #if sel == 1:
                        x[count] = row[0]
                        y[count] = row[1]
                        count += 1
                        sel=0
                    #sel += 1
                #y = y/314809.0
                print(x) 
                print(y)

                
        else:
            print("Invalid option")
    else:
        x=np.array([0 for i in range(0,number)])
        y=np.array([0 for i in range(0,number)])
        #filename = Path(path)
        with open(path,'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader) #skip header

            count=0
            sel=0
            for row in csv_reader:
                    #print(row)
                #if sel == 1:
                    x[count] = row[row0]
                    y[count] = row[row1]
                    count += 1
                    sel=0

                    if count == number: break
                #sel += 1
                #y = y/314809.0
            


    return x,y
    


def polinomialInterpolation(x,y):
   

    vander = mx.zerosSquareMatrix(len(x))

    for i in range(0,len(x)):
        vander[i][0] = 1

    count=0

    for i in range(1,len(x)):
        count +=1
        for j in range(0,len(x)):

            vander[j][i] = pow(x[j],count)
            
    

    res = mx.montante(vander,y)
    #res = np.linalg.solve(vander,y)
    #res=mx.gaussJordan(vander,y)
    #print(res)
    res2=res[1][::-1]
    #res2=res[::-1]
    print("Coeficientes del polinomio (a"+str(len(res2)-1)+ " hasta a0): ",res2)

    #f = lambda x: res2[0]*pow(x,4) + res2[1]*pow(x,3) + res2[2]*pow(x,2) + res2[3]*x +res2[4]

    #print("Prediccion (decesos acumulados) para el día domingo 19 de julio: ",f(124))


    f = lambda z,a,n: a*pow(z,n)
    points = np.linspace(x[0],x[-1])
    h=[0 for i in range(0,len(points))]

    #h = np.polyval(res2,points)

    count=0
    for p in points:
        suma = 0
        no = len(x) -1
        for i in range(0,len(res2)):
            suma += f(p,res2[i],no)
            no -= 1
        h[count] = suma
        count+=1

    """ plt.plot(points, h)
    plt.plot(x, y, 'ro', mew=2)
    plt.show() """

    return points,h

def arg_prod(i, j):
   
    x_sim = sympy.symbols('x')
    return (x_sim-x[i]) / (x[j]-x[i]) if i != j else 1

def interpolacion_lagrange(x, y, num_puntos=100):
   
    
    x_sim = sympy.symbols('x')
    
    
    points = len(x)
    
   
    lj = []
    for k in range(points):
        lk = np.prod([arg_prod(i, k) for i in range(points)])
        lj.append(lk)
    
    pol = sum(y*lj)
    pol = sympy.simplify(pol)
    print(pol)

    r=pol.subs(x_sim,1.5)
    print(r)
    #print("Prediccion (decesos acumulados) para el día domingo 19 de julio: ",r.evalf())
    
   
    x_test = np.linspace(min(x), max(x), num_puntos)
   
    y_pol = [pol.subs(x_sim, i) for i in x_test]
    
    return x_test, y_pol

def Newt_prod(i,j,f,arr):
    x=arr

    x_sim = sympy.symbols('x')
    
    return  f[j]*(x_sim - x[i]) if i==0 else (x_sim - x[i])

def interpolacion_Newton(x,y):
    x_sim = sympy.symbols('x')

    points = len(x)

    coef = []
    
    for l in y:
        coef.append(l)



    y_k = []
    x_count = 1
    
    while(points>0):
        y_k.append(coef[0])
        for i in range(0,points-1):
            
            coef[i] = (coef[i+1] - coef[i])/(x[i+x_count] - x[i])
            print(coef[i+1] - coef[i],x[i+x_count] - x[i], coef[i])

        points -= 1
        x_count += 1

    
    
    del coef

    points = len(x)
    
    lj = []
    
    x_count = 0
    
    for j in range(0,points):
        lk = np.prod([Newt_prod(i,j,y_k,x) for i in range(0,x_count)])
        lj.append(lk)
        x_count += 1
    
    lj[0] = lj[0]*y_k[0]

    
    
    pol = sum(lj)

   
   
   
    pol = sympy.simplify(pol)

    print("El polinomio de interpolación de Newton es: ",pol)


    r=pol.subs(x_sim,4)
    print(r)
    #print("Prediccion (casos positivos acumulados) para el día domingo 16 de agosto: ",r.evalf())
   
    x_test = np.linspace(x[0],x[-1])
   
    y_pol = [pol.subs(x_sim, i) for i in x_test]
    
    return x_test, y_pol



def min_squares(x,y,pol_order):

    s = np.zeros((pol_order+1,pol_order+1))
    v = np.zeros(pol_order+1)
    
    for i in range(0,len(s)):
        if i == 0:
            v[i] = sum(y)
        else:
            v[i] = sum(y*pow(x,i))

        for j in range(0,len(s[0])):

            if j==0 and i == 0:
                s[0][0] = len(x)
            else:
                s[i][j] = sum(pow(x,j+i))
                
    #print(v)
    #print(s)
    res = mx.montante(s,v)
    #res = mx.gaussJordan(s,v)
    #for r in res:
     #   print(r[0])
    x_sim = sympy.symbols('x')
    print(res)

    lj = []
    for j in range(0,pol_order+1):
        lk = np.prod([res[1][j]*x_sim**j])
        #lk = np.prod([res[j]*x_sim**j])
        lj.append(lk)

    pol = sum(lj)

    print("El polinomio ajustado por mínimos cuadrados es: ",pol)

    r=pol.subs(x_sim,1.5)
    print(r)
    #print("Prediccion (Casos confirmados) para el día domingo 16 de agosto: ",r*491379)

    x_test = np.linspace(x[0],x[-1])
   
    y_pol = [pol.subs(x_sim, i) for i in x_test]
    
    return x_test, y_pol


#x,y = dataAcquisition(None,'data.csv',4)


#x = np.array([1.,3.,4.,8.])
#y = np.array([2.,3.,2.,10.])

#x = np.array([0.4,2.5,4.3,5.0,6.0])
#y = np.array([1.,0.5,2.,2.55,4.])

""" k,l=polinomialInterpolation(x,y) 
#k,l=np.polyfit(x,y,deg=1,)
x_test,y_pol=interpolacion_lagrange(x,y) """

""" plt.plot(k, l)
plt.scatter(x, y)
plt.legend(['Polinomio', 'Datos'], loc='best')
plt.show()

plt.plot(x_test, y_pol)
plt.scatter(x, y)
plt.legend(['Lagrange', 'Datos'], loc='best')
plt.show() """


""" plt.plot(x_test, y_pol)
plt.scatter(x, y)
plt.legend(['Newton', 'Datos'], loc='best')
plt.show()  """

""" x_test, y_pol = min_squares(x,y,2)
x_test1, y_pol1 = min_squares(x,y,1)
x_test2, y_pol2 = min_squares(x,y,4)
 """
""" plt.plot(x_test, y_pol)
plt.plot(x_test1, y_pol1)
plt.plot(x_test2, y_pol2)
plt.scatter(x, y)
plt.legend(['Pol 2o','Pol. 1er', 'Pol. 3er', 'Datos'], loc='best')
plt.show() """

#x,y = dataAcquisition(None,'data.csv',208,2,3)
#print(x,y)
""" y=y/491379
x=x/208 """
#x_test, y_pol=interpolacion_Newton(x,y)

""" x = np.array([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
y = np.array([0.0,0.1002,0.2013,0.3045,0.4108,0.5211,0.6367,0.7586,0.8881,1.0265,1.1752])
x_test, y_pol=min_squares(x,y,3) """

""" x1,y1 = dataAcquisition(None,'data.csv',208,2,3)
x1 = x1/100000.0
x_test1, y_pol1=min_squares(x1,y1,3)

x2,y2 = dataAcquisition(None,'data.csv',4,4,5)
x_test2, y_pol2=interpolacion_Newton(x2,y2)

x3,y3 = dataAcquisition(None,'data.csv',148,6,7)
x_test3, y_pol3=min_squares(x3,y3,2) """

""" x = np.array([1,3,5,7,9])
y = np.array([5,3,7,13,25])

x_test, y_pol = min_squares(x,y,2)

plt.plot(x_test, y_pol)
plt.scatter(x, y)
plt.legend(['Min. cuadrados', 'Datos'], loc='best')
plt.title('Casos confirmados')
plt.show()  """

""" plt.plot(x_test1, y_pol1)
plt.scatter(x1, y1)
plt.legend(['Mínimos cuadrados', 'Datos'], loc='best')
plt.title('Casos confirmados')
plt.show() 

plt.plot(x_test2, y_pol2)
plt.scatter(x2, y2)
plt.legend(['Newton', 'Datos'], loc='best')
plt.title('Decesos')
plt.show() 

plt.plot(x_test3, y_pol3)
plt.scatter(x3, y3)
plt.legend(['Mínimos cuadrados', 'Datos'], loc='best')
plt.title('Decesos')
plt.show()  """

""" plt.figure()

plt.subplot(221)
plt.plot(x_test, y_pol)
plt.scatter(x, y)
plt.legend(['Newton', 'Datos'], loc='best')
plt.title('Casos positivos')

plt.subplot(222)
plt.plot(x_test1, y_pol1)
plt.scatter(x1, y1)
plt.legend(['Mínimos cuadrados', 'Datos'], loc='best')
plt.title('Casos positivos')

plt.subplot(223)
plt.plot(x_test2, y_pol2)
plt.scatter(x2, y2)
plt.legend(['Newton', 'Datos'], loc='best')
plt.title('Defunciones')

plt.subplot(224)
plt.plot(x_test3, y_pol3)
plt.scatter(x3, y3)
plt.legend(['Mínimos cuadrados', 'Datos'], loc='best')
plt.title('Defunciones')

plt.show() """

y_g = -10
y_r = 0
x_g = -10
x_r = 0
beta = math.atan((y_g - y_r)/(x_g - y_r))

print((beta*180)/math.pi)


y_dif = y_g - y_r
x_dif = x_g - x_r


beta = math.atan(y_dif/x_dif)



if x_dif < 0 :
    beta = math.pi + beta
elif x_dif < 0 and y_dif < 0:
    beta = math.pi - beta 


print((beta*180)/math.pi)
