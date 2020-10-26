
def BirgeVieta(a, n, zeros):
    ep = 1e-10
    itmax = 100

    nx = 0

    if(n <= 1):
        return
    
    x = 0

    for m in range(n,1,-1):
        for i in range(1,itmax+1):
            p = a[0]
            d = p
            for j in range(1,m):
                p = p*x + a[j]
                d = d*x + p
            p = p*x + a[m]
            d = -p/d if d else -p
            x += d
            if(abs(d) <= ep*abs(x) ): break

        if(i == itmax):
            print("Número de iteraciones excedido")
            return

        nx += 1
        zeros[nx] = x

        for j in range(1,m):
            a[j] += a[j-1]*x
    
    nx += 1
    zeros[nx] = -a[1]/a[0]

    return nx


n = 3
ax = [1,-11,32,-22]
zeros = [0]*(n+1)

nx = BirgeVieta(ax,n,zeros)
print("\nRaíces encontradas => \n")
for i in range(1, nx+1):
    print("R" + str(i) + " = ", zeros[i])

if(nx <= 0):
    print("No existen raices reales")