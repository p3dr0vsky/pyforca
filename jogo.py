from random import randint
palavras = ['PYTHON', 'HTML', 'JAVA']
esc = randint(0, 2)
escolha = palavras[esc]


def linha(tam=42):
    print('~' * tam)


def procurar(escolha, palpite):
    pos = list()
    for i in range(0, len(escolha)):
        if palpite in escolha[i]:
            pos.append(palpite)
    return pos


linha()
print('BEM VINDO AO JOGO DA FORCA'.center(42))
linha()
u = list()
for c in range(len(escolha)):
    u.append('_')
print(f'A palavra escolhida tem o seguinte tamanho: {u}')
while True:
    palpite = str(input('Digite um letra: ')).upper()
    if palpite in escolha:
        print(f'A letra {palpite} não se encontra na palavra')
        print('_' * len(escolha))
    if '_' not in u:
        print('PARABÉNS! CONSEGUIU ADIVINHAR A PALAVRA!')
        print(escolha)
        break







