

#-------------------------------------------
#Programa para convertir números decimales a binarios y viceversa
#Marcos Rocha

#-------------------------------------------

""" El código esta compuesto por 3 funciones, una para transformar el número decimal a binario, 
una para meter a un arreglo el número binario como caracteres separados y una funcion para 
transformar de binario a decimal  """



#1er función (Transformar de decimal a binario)

#"def" se utiliza para indicar que estamos definiendo una funcion, 
#despues sigue el nombre de la funcion (en este caso "binario" es el nombre)
#y el nombre debe estar seguido de los parentesis, en los cuales indicamos que 
#parametros seran introducidos a la funcion
def binario(dec_num):
    binary = '' #se define una variable llamada "binary" la cual por las comillas ('') se indica que esta vacia
                #y es de tipo char
    while dec_num // 2 != 0: #Se crea un ciclo while con la condicion de que se repitan las instrucciones
                             #hasta que se complete la condición dec_num // 2 != 0
                             #el simbolo // significa cuantas veces cabe un numero en otro numero, en este caso
                             #cuantas veces cabe el 2 en el numero ingresado
        binary = str(dec_num % 2) + binary #en la variable binary guardamos el módulo del número
        dec_num = dec_num // 2 #realizamos la operacion condicional para saber si ya se cumplio o hay que seguir
                                #operando
    return str(dec_num) + binary #Al terminar el ciclo while la funcion regresa el número binario como una cadena de caracteres

def split(word): #definimos una funcion
    return [char for char in word] #a una palabra la separamos en caracteres y la funcion regresa los caracteres 

def decimal(bin_num): #definimos la funcion para convertir a decimal
    count = 0 #inicializamos una variable que no servira de contador
    sum = 0 #inicializamos una varibale en la cual guardaremos el valor de una suma
    a = [] #inicializamos una variable de tipo arreglo, las llaves cuadradas indican arreglo
    a = split(bin_num) #llamamos la funcion que separa el número binario en caracteres y los guardamos en el arreglo a
    pot = len(a) - 1 
    
    while(count < len(a)): #Iniciamos un ciclo while que seguira operando hasta que el contador "count" sea 
                            #igual al tamaño del arreglo a. "len" es un operador que regresa el tamaño de un vector 

        sum += int(a[count])*(2**pot) #realizamos la operacion como la que mostro Cuevas en la presentacion
        pot -= 1    #reducimos en 1 el orden de la potencia a la que se eleva el número 2
        count += 1  #aumentamos en 1 el contador de la condicion

    return sum #regresamos el valor de la suma


#Aqui comienza la seccion principal del codigo

print("Convertir de: ")
print("1 = Decimal a binario \n")
print("2 = Binario a decimal \n")

val = input("Selección = ") #imprime el texto, se lee el valor introducido y se guarda en val la seleccion de conversion
num = input("Número a convertir = ") #imprime texto, se lee el numero introducido y se guarda en la variable num 

#Abrimos funciones if para solo realizar la conversion solicitada

if(val == "1"): #si la opcion introducida es 1
                #se imprime el texto y se llama la funcion con la cual se convierte de decimal a binario
    print("El número decimal en binario es: ", binario(int(num)))

elif(val == "2"):#si la opcion introducida es 2
                #se realiza la conversion a decimal
    
    print("El número binario en decimal es: ", decimal(num))

else: #si no se introduce un valor adecuado de las opciones, se imprime el texto
    print("Opción no valida")
    

