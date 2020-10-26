import math


def biseccion(f,a,b,N):
   
    if f(a)*f(b) >= 0:
        print("El intervalo no es correcto")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Solución exacta encontrada")
            return m_n
        else:
            print("No es posible encontrar la raíz")
            return None
    return (a_n + b_n)/2.0


def falsa(f, a, b, N): 
    if f(a) * f(b) >= 0: 
        print("El intervalo no es correcto") 
        return None
    
    a_n = a
    b_n = b
    m_n = a
    for n in range(1,N+1): 
    
        m_n = b_n - (a_n * f(b_n) - b_n * f(b_n))/ (f(a_n) - f(b_n)) 
           
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Solución exacta encontrada")
            return m_n
        else:
            print("No es posible encontrar la raíz")
            return None
    return (a_n * f(b_n) - b_n * f(a_n))/ (f(b_n) - f(a_n))

def secante(f,xi,xo,N):
    
    x_1 = xi
    x_0 = xo
    for n in range(1,N+1):
        x_2 = x_1 - (f(x_1)*(x_0 - x_1)/(f(x_0) - f(x_1)))
       
        f_m_n = f(x_2)
        x_0 =  x_1
        x_1 = x_2
        
        if f_m_n == 0:
            print("Solución exacta encontrada")
            return x_2
        

    return x_1 - f(x_1)*(x_0 - x_1)/(f(x_0) - f(x_1))

i = 3
j = 0
xi = 1.0
xo = 0.0
n = 10

f = lambda x: math.exp(-x) - x
#f = lambda x: x**3

print("Biseccion: ", biseccion(f, i, j, n))
print("Falsa pos.: ", falsa(f, i, j, n))
print("Secante: ", secante(f,xi,xo,n))