def posicoes(c, p):
    l = list()
    for x in range(len(p)):
        if p[x] == c:
            l.append(x)
    return l


print(posicoes('a', 'palavra'))


def repete(c, nv):
    l = list()
    for x in range(nv):
        l.append(c)
    return l


print(repete('c', 3))


def subtitui(c, p, str=False):
    pos = posicoes(c, p)
    u = repete('_', len(p))
    for x in pos:
        u[x] = c
    if str:
        u = ''.join(u)
    return u


print(subtitui('a', 'palavra', False))
