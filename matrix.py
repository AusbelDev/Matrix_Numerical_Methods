import numpy as np
""" X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]] """

""" X = [[1,2],
    [2,3],
    [3,4]] """
""" 
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]] """

""" Y = [[1,2],
    [2,3],
    [3,4]]
 """
""" Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]] """

#X = [[1,3,4],[2,7,3],[2,8,6]]
X = [[11,11,5],
    [2.5,3,2],
    [2.1,3,2]]

V = [600,130,110]

#print("Matriz X tiene dimensiones: " +  str(len(X)) + "x" + str(len(X[0])))

#print("Matriz Y tiene dimensiones: " +  str(len(Y)) + "x" + str(len(Y[0])) + "\n")

def matrixSum(X,Y):

    if(len(X) == len(Y) and len(X[0]) == len(Y[0])):

        result = [[ 0 for y in range( len(Y[0]) ) ] for x in range( len(X) )]

        for i in range(len(X)):
        
            for j in range(len(X[0])):
                result[i][j] = X[i][j] + Y[i][j]

    else:
        print("No es posible realizar la suma. Las matrices deben ser de las mismas dimensiones \n")

    return result

def matrixMult(X,Y):
    if(len(X[0]) == len(Y)):

        result2 = [ [ 0 for y in range( len(Y[0]) ) ] for x in range( len(X) ) ]

        for i in range(len(X)):
        
            for j in range(len(Y[0])):
                
                for k in range(len(Y)):
                    result2[i][j] += X[i][k] * Y[k][j]


    else:
        print(" \n No es posible realizar la multiplicación. El número de columnas de la matriz X debe ser igual al número de filas de la matriz Y \n")

    return result2

def identity(n):
    identidad=[[0 for x in range(n)] for y in range(n)]
    for i in range(0,n):
        
        identidad[i][i] = 1
    
    return identidad

def zerosSquareMatrix(n):
    zeros=[[0 for x in range(n)] for y in range(n)]

    return zeros

def matrixMultScalar(X,a):
    
    escalar = [ [ 0 for y in range( len(X[0]) ) ] for x in range( len(X) ) ]

    for i in range(len(X)):
        
        for j in range(len(X[0])):

            escalar[i][j] = X[i][j] * a
   
    return  escalar

def transpose(X):
    
    trans = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
    
    return trans

def determinant(X):
   
    n = len(X)
    
    for d in range(n): 
        
        for i in range(d+1,n): 
            
            if X[d][d] == 0: 
                
               X[d][d] == 1.0e-18
            
            p = X[i][d] / X[d][d] 
            
            for j in range(n): 
                
                X[i][j] = X[i][j] - p * X[d][j]
     
   
    prod = 1.0

    for i in range(n):
        
        prod *= X[i][i] 

    return prod
 

def matrizMenor(m,i,j):

    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def cofMatrix(X,n):
    
    C = [ [ 0 for y in range( len(X[0]) ) ] for x in range( len(X) ) ]
   
    
    for i in range(n):

        for j in range(n):

            cof = matrixMenor(X,i,j)

            m = determinant(cof)

            C[i][j] = ((-1)**(i+j))*m
    
    return C


def adjoint(X):
    
    X = cofMatrix(X,len(X))

    A = transpose(X)

    return A

def inverse(X):

    adj = adjoint(X)

    det = determinant(X)

    if det != 0:
        f = 1/det

        inv = matrixMultScalar(adj,f)
    else:
        print("Det = 0; No existe la inversa")

    return inv


def gaussJordan(X, V):

    m = len(V)
    x = [ 0 for x in range( len(X) ) ]
    
    det = determinant(X)
    
    if det != 0.0:

        for k in range(0, m):
            for r in range(k+1, m):
                factor=(X[r][k]/X[k][k])
                V[r]=V[r]-(factor*V[k])
                for c in range(0,m):
                    X[r][c]=X[r][c]-(factor*X[k][c])

        x[m-1]=V[m-1]/X[m-1][m-1]
        
        for r in range(m-2, -1, -1):
            suma = 0
            for c in range(0,m):
                suma=suma+X[r][c]*x[c]
            x[r]=(V[r]-suma)/X[r][r]  
        
        return x
    
    else:
        return print("El sistema no tiene solución")


def montante(Xi,V):
    
    div=1
    v = [ 0 for x in range( len(Xi) ) ]
    #X = np.append(X,V,axis=1)
    X = [ [ 0 for y in range( len(Xi[0]) + 1 ) ] for x in range( len(Xi) ) ]
    for i in range(0,len(X)):
        for j in range(0,len(X[0])-1):
            X[i][j] = Xi[i][j]

    for l in range(0,len(X)):
        lon = len(X[0])-1
        X[l][lon] = V[l]
    
    for i in range(0,len(X)):
        for j in range(0,len(X[0])):
            if i==j:
                for r in range(0,len(X)):
                    for c in range(j+1,len(X[0])):
                        if r!=i:
                            #print(X[i][j],"*",X[r][c], "-" ,X[i][c],"*",X[r][j], "/", div)
                            X[r][c] = (X[i][j]*X[r][c] - X[i][c]*X[r][j])/div
                            #print("=",X[r][c])
                            
                        
                div = X[i][j] 
    
    for l in range(0,len(X)):
        lon = len(X[0])-1
        v[l] = X[l][lon]/X[len(X)-1][lon-1]          
    
    #for r in X: print(r)
    
    return X,v
                
           
def jacobi(Xi, X0, V,tol,it):
    count = 0
    v = [ 0 for x in range( len(Xi) ) ]
    #X = [ [ 0 for y in range( len(Xi[0]) + 1 ) ] for x in range( len(Xi) ) ]
    maxvalues=0
    for i in range(0, len(Xi)):
        val = 0
        for j in range(0,len(Xi[0])):
            if i != j:
                val += abs(Xi[i][j])

        if abs(Xi[i][i]) > val:
            maxvalues += 1
            
    if maxvalues < len(Xi):
        print("La matriz no es diagonalmente dominante, no se asegura la convergencia")

    e = 1

    for i in range(0, len(Xi)):
        div = Xi[i][i]
        V[i][0] = V[i][0]/div
        for j in range(0,len(Xi[0])):
            Xi[i][j] = (-1)*Xi[i][j]/div
        Xi[i][i] = 0

    
    while(count < it):

        a = matrixMult(Xi,X0)
        a = matrixSum(a,V)

        for i in range(0,len(v)):
            v[i] = abs(a[i][0] - X0[i][0])
            X0[i][0] = a[i][0]
        e = max(v)
        count += 1
        if e < tol:
            break

    print("Número de iteraciones: ", count)
    print("Error")
    print(v)
    print("Vector solución")
    print(X0)


def GaussSeidel(Xi, X0, V,tol,it):
    count = 0
    v = [ 0 for x in range( len(Xi) ) ]
    f = [ [ 0  for x in range( len(Xi) ) ]]
    a = [ [ 0 ] for x in range( len(Xi) ) ]
    maxvalues=0
    for i in range(0, len(Xi)):
        val = 0
        for j in range(0,len(Xi[0])):
            if i != j:
                val += abs(Xi[i][j])

        if abs(Xi[i][i]) > val:
            maxvalues += 1
            
    if maxvalues < len(Xi):
        print("La matriz no es diagonalmente dominante, no se asegura la convergencia")

    e = 1

    for i in range(0, len(Xi)):
        div = Xi[i][i]
        V[i][0] = V[i][0]/div
        for j in range(0,len(Xi[0])):
            Xi[i][j] = (-1)*Xi[i][j]/div
        Xi[i][i] = 0

    
    while(count < it):
        row = 0
        while(row < len(Xi)):

            for i in range(0,len(Xi[0])):
                f[0][i] = Xi[row][i]

            print(f,"\n")
            b = matrixMult(f,a)
            #for i in range(0,len(Xi)):
                    
                
                    
            a[row][0] = b[0][0] + V[row][0]
            #print(a)
                 
            
            row += 1
            #print(row)

        for i in range(0,len(v)):
            v[i] = abs(a[i][0] - X0[i][0])
            X0[i][0] = a[i][0]
        
        e = max(v)
        
        count += 1
        
        if e < tol:
            break

    print("Número de iteraciones: ", count)
    print("Error")
    print(v)
    print("Vector solución")
    print(X0)   
    


#print(montante(X,V))

#X = [[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]]
#V = [[6],[25],[-11],[15]]
#X0 = [[0],[0],[0],[0]]

""" X = [[3.0,-0.1,-0.2],[0.1,7.0,-0.3],[0.3,-0.2,10.0]]
V = [[7.85],[-19.3],[71.40]]
X0 = [[0],[0],[0]]
#jacobi(X,X0,V,0.001,150)
GaussSeidel(X,X0,V,0.001,150) """

""" x = [[165,13695,1511015,187553025,24831718307],
    [13695,1511015,187553025,24831718307,3.42466e+12],
    [1511015,187553025,24831718307,3.42466E+12,4.85803E+14],
    [187553025,24831718307,3.42466E+12,4.85803E+14,7.03488E+16],
    [24831718307,3.42466E+12,4.85803E+14,7.03488E+16,1.03488E+19]]
v=[224541,30759874,4311256374,6.15678E+11,8.92938E+13]

print(gaussJordan(x,v)) """