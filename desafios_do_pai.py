# # Faz uma função que conte o numero de ocorrências de uma letra numa string
# # exemplo:
# # n = ocorre('a', 'palavra')
# # print(n)
# # R: 3
#
# # def conta(c, p):
# #     t = 0
# #     for x in p:
# #         if x == c:
# #             t += 1
# #     return t
# #
# #
# # def conta2(c, p):
# #     t = 0
# #     for i in range(0, len(p)):
# #         if p[i] == c:
# #             t += 1
# #     return t
# #
# #
# def teste_ocorre():
#     if nc == 3:
#         print('passou no test')
#     else:
#         print('falhou')
# #
# #
# # print(conta('a', 'palavra'))
# # print(conta2('a', 'palavra'))
# #
# #
# teste_ocorre()
#
# palavra = 'palavra'
# c = 'a'
# nc = palavra.count('a')
# print(nc)


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


def substitui(p, c, string=False):
    pos = posicoes(c, p)
    u = repete('_', len(p))
    for x in pos:
        u[x] = c
    if string:
        u = "".join(u)
    return u


print(substitui('palavra', 'a', True))

