from random import randint
from time import sleep
palavras = ['PYTHON', 'HTML', 'JAVA', 'PHP', 'C++', 'RUST', 'GOLANG', 'ELIXRI', 'ERLANG']
esc = randint(0, 8)
escolha = palavras[esc]
tentativas = 5


def linha(tam=42):
    print('~' * tam)


def posicoes(c, p):
    lista = list()
    for x in range(len(p)):
        if c == p[x]:
            lista.append(x)
    return lista


def repete(c, nr):
    lista = list()
    for i in range(nr):
        lista.append(c)
    return lista


def substitui(p, c, s, string=False):
    pos = posicoes(c, p)
    for x in pos:
        s[x] = c
    if string:
        s = "".join(s)
    return s


linha()
print('BEM VINDO AO JOGO DA FORCA'.center(42))
linha()
sleep(1)
print('AQUI ESTÁ A PALAVRA:')
estado = repete('_', len(escolha))
print("".join(estado))
sleep(1)
while True:
    palpite = str(input('Digite uma letra: ')).upper()
    sleep(1)
    if palpite in escolha:
        linha()
        print('PARABÉNS!ACERTOU!')
        estado = substitui(escolha, palpite, estado)
        print("".join(estado))
        linha()
        sleep(1)
    else:
        tentativas -= 1
        linha()
        print('ERROU tente outra vez')
        print(f'TEM MAIS {tentativas} TENTATIVAS')
        print("".join(estado))
        linha()
        sleep(1)
    if tentativas == 0:
        linha()
        print('PERDEU POR DEMASIADAS TENTATIVAS'.center(42))
        print(f'A palavra era {escolha}'.center(42))
        linha()
    if '_' not in estado:
        linha()
        print(f'PARABÉNS!! ACERTOU A PALAVRA:\nA palavra é {escolha}'.center(42))
        linha()
        break







