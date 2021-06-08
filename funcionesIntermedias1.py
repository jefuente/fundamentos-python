import random
def randInt(min='' , max='' ):
    if(min==''and max==''):
        num = round(random.random() *100)
    if(min==''and max!=''):
        num = round(random.random() *(100-max))   
    if(min!=''and max==''):
        num = round(random.random() *(100-min)+min)  
    if(min!=''and max!=''):
        num = round(random.random() *(500-min)+min)  
    return num
print(randInt()) 		    # debería imprimir un número aleatorio entre 0 a 100
print(randInt(max=50)) 	    # debería imprimir un número aleatorio entre 0 a 50
print(randInt(min=50)) 	    # debería imprimir un número aleatorio entre 50 a 100
print(randInt(min=50, max=500))    # debería imprimir un número aleatorio entre 50 y 500

