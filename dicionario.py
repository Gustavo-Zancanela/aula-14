dicionario = {'gato':'chat',
            'cachorro':'chien',
            'cavalo':'chieval'}

telefones = {'Chefe':45467889,
            'Suzy':908765544}

palavras = {'gato', 'leão', 'cavalo'}

dicionario_vazio = {}

print(dicionario)
print(telefones)
print(dicionario_vazio)
print(dicionario['gato'])
print(telefones['Suzy'])

for palavra in palavras:
    if palavra in dicionario:
        print(palavra, '-->', dicionario[palavra])
    else:
        print(palavra, 'não está no dicionário')

for chave in dicionario.keys():
    print(chave)

for valores in dicionario.values():
    print(valores)

for portugues, frances in dicionario.items():
    print(portugues, '=', frances)

for chaves in sorted(dicionario.keys()):
    print(chaves)

dicionario['gato'] = 'miau'
dicionario['cisne'] = 'cygne'
dicionario.update({'pato':'cannard'})
print(dicionario)

d1 = {'Adam Smith' : 'A', 'Judite Silva' : 'B+'}
d2 = {'Marli Santos' : 'A', 'Paulo José' : 'C'}
d3 = {}
for item in (d1,d2):
    d3.update(item)
print(d3)

dicionarionovo = dicionario.copy()
print(dicionarionovo)

del dicionario['cachorro']
print(dicionario)

dicionario.popitem() # deleta o último item
print(dicionario)