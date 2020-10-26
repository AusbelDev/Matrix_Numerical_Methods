

#-------------------------------------------
#Programa para convertir números decimales a binarios y viceversa
#Marcos Rocha

#-------------------------------------------




#

#"def" se utiliza para indicar que estamos definiendo una funcion, 
#despues sigue el nombre de la funcion (en este caso "binario" es el nombre)
#y el nombre debe estar seguido de los parentesis, en los cuales indicamos que 
#parametros seran introducidos a la funcion
def binario(num, base):
    binary = '' #se define una variable llamada "binary" la cual por las comillas ('') se indica que esta vacia
                #y es de tipo char
    while num // base != 0: #Se crea un ciclo while con la condicion de que se repitan las instrucciones
                             #hasta que se complete la condición dec_num // 2 != 0
                             #el simbolo // significa cuantas veces cabe un numero en otro numero, en este caso
                             #cuantas veces cabe el 2 en el numero ingresado
        binary = str(num % base) + binary #en la variable binary guardamos el módulo del número
        num = num // base #realizamos la operacion condicional para saber si ya se cumplio o hay que seguir
                                #operando
    return str(num) + binary #Al terminar el ciclo while la funcion regresa el número binario como una cadena de caracteres

def split(word): #definimos una funcion
    return [char for char in word] #a una palabra la separamos en caracteres y la funcion regresa los caracteres 

def decimal(bin_num, base): #definimos la funcion para convertir a decimal
    count = 0 #inicializamos una variable que no servira de contador
    sum = 0 #inicializamos una varibale en la cual guardaremos el valor de una suma
    dec = 0
    flag = False
    a = [] #inicializamos una variable de tipo arreglo, las llaves cuadradas indican arreglo
    a1 = []
    a2 = []
    a = split(bin_num) #llamamos la funcion que separa el número binario en caracteres y los guardamos en el arreglo a
    pot = len(a) - 1
    
    while(count < len(a)): #Iniciamos un ciclo while que seguira operando hasta que el contador "count" sea 
                            #igual al tamaño del arreglo a. "len" es un operador que regresa el tamaño de un vector 
        
        
        sum += float(a[count])*(base**pot) 
        
        pot -= 1    #reducimos en 1 el orden de la potencia a la que se eleva el número 2
        count += 1  #aumentamos en 1 el contador de la condicion
        
      
        
    
    return sum #regresamos el valor de la suma


base = input("Ingrese a que base quiere convertir = ")
base_num = input("Ingrese la base en la que se encuentra el número a convertir = ")
num = input("Ingrese el número = ")

new= decimal(num,float(base_num))
print(new)
print("El número en base " + base + " es: " + binario(int(new), int(base)))

