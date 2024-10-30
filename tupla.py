tupla = (1,2,4,8)
tupla2 = 1.,.5,.25,.125

print(tupla)
print(tupla2)

minhatupla = (1,10,100,1000)
print(minhatupla[0])
print(minhatupla[-1])
print(minhatupla[1:])
print(minhatupla[:-2])
for i in minhatupla:
    print(i)

minhatupla2 = (1,10,100)
t1 = minhatupla2 + (1000, 10000)
t2 = minhatupla2*3
print(len(t2))
print(t1)
print(t2)
print(10 in minhatupla2)
print(-10 not in minhatupla2)

tup = 1,2,3,2,4,5,6,2,7,2,8,
duplicado = tup.count(2)
print(duplicado)

minhatupla3 = tuple((1,2,'senai'))
print(minhatupla3)
lista = [2,4,6]
print(lista)
print(type(lista))
tup = tuple(lista) #list converte em lista
print(tup)