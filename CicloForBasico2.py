#1. Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
#Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

def biggie_size(a=[]):
    for i in range(0, len(a)):
        if a[i]>0:
            a[i]="big"
    return a
lista =[1,-3,4,-6,-4,7]
print(biggie_size(lista))

#2. Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. 
# (Tenga en cuenta que cero no se considera un número positivo).
#Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
#Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve

def count_positives(a=[]):
    contador=0
    for i in range(0, len(a)):
        if a[i]>0:
            contador+=1
    a[len(a)-1]=contador    
    return a
lista =[1,6, -4, -2, -7, -2]
print(count_positives(lista))

#3. Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
#Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
#Ejemplo: sum_total ([6,3, -2]) debería devolver 7

def sum_total(a=[]):
    suma=0
    for i in range(0, len(a)):
        suma+=a[i]   
    return suma
lista =[1,2,3,4]
print(sum_total(lista))

#4. Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
#Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

def promedio(a=[]):
    suma=0
    for i in range(0, len(a)):
        suma+=a[i]   
    media = suma/len(a)    
    return media
lista =[1,2,3,4]
print(promedio(lista))

#5. Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
#Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
#Ejemplo: longitud ([]) debería devolver 0

def longitud(a=[]):   
    return len(a)
lista =[1,2,3,4]
print(longitud(lista))


#6. Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
#Ejemplo: mínimo ([]) debería devolver False

def minimo(a=[]):
    if a ==[]:
        return False
    min=a[0]
    for i in range(0, len(a)):
        if a[i]<min:
            min=a[i]
    return min
lista =[1,2,3,4]
vacia=[]
print(minimo(lista))
print(minimo(vacia))

#7. Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. 
# Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
#Ejemplo: máximo ([]) debería devolver False

def maximo(a=[]):
    if a ==[]:
        return False
    max=a[0]
    for i in range(0, len(a)):
        if a[i]>max:
            max=a[i]
    return max
lista =[1,2,3,4]
vacia=[]
print(maximo(lista))
print(maximo(vacia))

#8. Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
#Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}

def ultimate_analysis(a=[]):
    if a ==[]:
        return False
    suma=0
    min=max=a[0]
    for i in range(0, len(a)):
        suma+=a[i]
        if a[i]<min:
            min=a[i] 
        if a[i]>max:
            max=a[i]      
    media = suma/len(a) 
    diccionario={'total': suma, 'promedio': media, 'minimo': min, 'maximo': max, 'longitud': len(a)} 
    return diccionario
lista =[1,2,3,4]
print(ultimate_analysis(lista))



#9. Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
#Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]

def reverse_list(a=[]):
    mitad=int(len(a)/2)
    for i in range(0, mitad): #hasta el largo de la mitad
        b=a[len(a)-1-i] #comenzamos asignando a b el valor del ultimo elemento y vamos retrocediendo
        c=a[i]#comenzamos asignando a c el valor del primer elemento y vamos avanzando
        a[i]=b #asignamos al valor del indice 0 el valor del ultimo indice y vamos avanzando en indice hasta la primera mitad
        a[len(a)-1-i]=c #asignamos al valor del ultimo indice el valor del primer indice y vamos avanzando en indice hasta la primera mitad
    print(a)  
x= [37,2,1, -9, 5]    
reverse_list(x)