mytup = (1,2,3)
print(mytup[2])

tup = 1,2,3
a,b,c = tup
print(a * b * c)

mydictionary={'A' : 1, 'B' : 2}
copymydictionary = mydictionary.copy()
mydictionary.clear()
print(copymydictionary)

colors = {
    'branco': (255,255,255),
    'cinza': (128,128,128),
    'vermelho': (255,0,0),
    'verde': (0,128,0)
    }
for col, rgb in colors.items():
    print(col, ':', rgb)
