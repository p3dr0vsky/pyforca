from time import sleep
notas = list()
pc = pe = 0


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


linha()
cabeçalho('TESTE DE EQUAÇÕES')
linha()
p1 = str(input('PERGUNTA 1:\n'
               'Encontra o valor de t na equação:\n'
               '5t + 5 = 3t +7\n'
               't = '))

if p1 == '1':
    print('Acertou!!')
    notas.append(10)
    pc += 1
else:
    print('ERROU')
    pe += 1
print(linha())
sleep(1)
p2 = str(input('PERGUNTA 2:\n'
               'Encontra o valor de x na equação:\n'
               '3(2x+1) = −9\n'
               'x = '))
if p2 == '-2':
    print('Acertou!!')
    notas.append(10)
    pc += 1
else:
    print('ERROU')
    pe += 1
print(linha())
sleep(1)
p3 = str(input('PERGUNTA 3:\n'
               'Encontra o valor de x na equação:\n'
               '2(2x−5) = 3(x−1)−4\n'
               'x = '))
if p3 == '3':
    print('Acertou!!')
    notas.append(10)
    pc += 1
else:
    print('ERROU')
    pe += 1
print(linha())
sleep(1)
p4 = str(input('PERGUNTA 4:\n'
               'Encontra o valor de x na equação:\n'
               '5x – 1 = 3x + 11\n'
               'x = '))
if p4 == '6':
    print('Acertou!!')
    notas.append(10)
    pc += 1
else:
    print('ERROU')
    pe += 1
print(linha())
sleep(1)
p5 = str(input('PERGUNTA 5:\n'
               'Encontra o valor de z na equação:\n'
               '3(z−2)+10 = 2(2z+2)+2\n'
               'z = '))
if p5 == '-2':
    print('Acertou!!')
    notas.append(10)
    pc += 1
else:
    print('ERROU')
    pe += 1
print(linha())
sleep(1)
p6 = str(input('PERGUNTA 6:\n'
               'Encontra o valor de x na equação:\n'
               '5x−12 = 3\n'
               'x = '))
if p6 == '3':
    print('Acertou!!')
    notas.append(10)
    pc += 1
else:
    print('ERROU')
    pe += 1
print(linha())
sleep(1)
p7 = str(input('PERGUNTA 7:\n'
               'Encontra o valor de x na equação:\n'
               '3x+1 = x−3\n'
               'x = '))
if p7 == '-2':
    print('Acertou!!')
    notas.append(10)
    pc += 1
else:
    print('ERROU')
    pe += 1
print(linha())
sleep(1)
p8 = str(input('PERGUNTA 8:\n'
               'Encontra o valor de x na equação:\n'
               '3x+6(x+1) = 3(x+1)+5\n'
               'x = '))
if p8 == '1/3':
    print('Acertou!!')
    notas.append(10)
    pc += 1
else:
    print('ERROU')
    pe += 1
print(linha())
sleep(1)
p9 = str(input('PERGUNTA 9:\n'
               'Encontra o valor de x na equação:\n'
               '3x+4(−2x+1) = 3(x−5)+2(2x−7)−3\n'
               'x = '))
if p9 == '3':
    print('Acertou!!')
    notas.append(10)
    pc += 1
else:
    print('ERROU')
    pe += 1
print(linha())
sleep(1)
p10 = str(input('PERGUNTA 10:\n'
                'Encontra o valor de x na equação:\n'
                '2x + 8 = x + 13\n'
                'x = '))
if p10 == '5':
    print('Acertou!!')
    notas.append(10)
    pc += 1
else:
    print('ERROU')
    pe += 1
tot = sum(notas)
print(cabeçalho(F'TOTAL: {tot}%'))
print(cabeçalho(f'PERGUNTAS CERTAS: {pc}\n'
                f'PERGUNTAS ERRADAS: {pe}'))







