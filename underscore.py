class Underscore:
    def map(self, iterable, callback):
        # tu código aqui
        a=[]
        for i in iterable:          
            a.append(callback(i))
        return a
          
    def find(self, iterable, callback):
        # tu código aqui
        for i in iterable:
            if callback(i): 
                return i

    def filter(self, iterable, callback):
        # tu código aqui
        b=[]
        for i in iterable:
            if callback(i):
                b.append(i)
        return b
#print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # debe retornar [2,4,6]
#callback: lambda x: x%2==0
#calback(i): lambda i: i%2==0

    def reject(self, iterable, callback):
        # tu código 
        c=[]
        for i in iterable:
            if callback(i):
                c.append(i)
        return c
# has creado una libreria con 4 métodos
# se crea la instancia de la clase
_ = Underscore() # sí, estamos configurando una instancia a una variable que es un guión bajo
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# debe retornar [2, 4, 6] después que termines de implementar el código de arriba

print(_.map([1,2,3], lambda x: x*2)) # debe retornar [2,4,6]
print(_.find([1,2,3,4,5,6], lambda x: x>4)) # debe retornar el primer valor que es mayor que 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # debe retornar [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2!=0)) # debe retornar [1,3,5]