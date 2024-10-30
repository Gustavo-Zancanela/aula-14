try:
    valor = int(input('Digite um número: '))
    print('Resultado',1/valor)
except ValueError:
    print('Tipo errado')
except ZeroDivisionError:
    print('Divisão por zero não permitida')
except:
    print('Alguma outra exceção')
