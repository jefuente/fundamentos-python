# 1. TAREA: imprimir "Hola mundo"
print("Hola mundo")

# 2. imprimir "Hola Noelle!" con el nombre en una variable
nombre = "Julio"
print( "Mi nombre es", nombre )	# con una coma
print( "Mi nombre es "+ nombre )	# con un +

# 3. imprimir "Hola 42!" con un numero en una variable
numero = "42"
print( "Hola", numero)	# con una coma
print( "Hola " + numero )	# con un + - !Este debería darnos un error!

# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print(f'Me encanta comer {fave_food1} and {fave_food2}.' ) # con una cadena f
print("Me encanta comer {} and {}.".format(fave_food1, fave_food2))
