while True:
    try:
        valor = int(input('Digite um número: '))
        print('Resultado', 1/valor)
        break
    except (ValueError, ZeroDivisionError):
        print('Tipo errado ou divisão por zero')
    except:
        print('Alguma outra exceção')
