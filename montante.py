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
    
    for r in X: print(r)
    
    return X,v

t = [[4,3,-2],[1,-1,1],[2,1,3]]  
f=[5,3,-2]

X, V = montante(t,f)