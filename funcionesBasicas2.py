#1. Cuenta regresiva : crea una función que acepte un número como entrada. 
# Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).
#Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]

def cuentaRegresiva(a):
    lista = []
    for i in range(a, -1, -1):
        lista.append(i)
    return lista
print(cuentaRegresiva(5))

#2. Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.
#Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2

def print_and_return(a,b):
    print (a)
    return b
print(print_and_return(5,10))


#3. First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.
#Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)

def first_plus_length(a):
    return(a[0]+len(a))
b = [5, 4, 3, 2, 1, 0]
print(first_plus_length(b))

#4. Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo
#  los valores de la lista original que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva
#  la nueva lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False
#Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
#Ejemplo: values_greater_than_second ([3]) debería devolver False

def values_greater_than_second(a):
    if len(a)<2:
        return False
    lista = []
    j=0
    segundo = a[1]    
    for i in range(0, len(a)):
        if (a[i]>segundo):
            lista.append(a[i])
            j+=1
    print(j)        
    return lista
x=[7,5,4,9,1,4,2,7,9,2]  
y=[8]
print(values_greater_than_second(x))
print(values_greater_than_second(y))

#5. Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor.
#  La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
#Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
#Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]

def length_and_value(tamano, valor):
    lista = []
    for i in range(0, tamano):
        lista.append(valor)  
    print(lista)         
    return lista
tam = 6 
val = 7
length_and_value(tam, val)
