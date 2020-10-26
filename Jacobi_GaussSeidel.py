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
    
X = [[3.0,-0.1,-0.2],[0.1,7.0,-0.3],[0.3,-0.2,10.0]]
V = [[7.85],[-19.3],[71.40]]
X0 = [[0],[0],[0]]
#jacobi(X,X0,V,0.001,150)
GaussSeidel(X,X0,V,0.001,150)