import turtle

# Configuração inicial
wn = turtle.Screen()
wn.bgcolor("white")

# Criar uma tartaruga
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed(2)

# Função para animação


def animate():
    for _ in range(36):  # 36 passos para fazer um círculo completo
        t.forward(10)
        t.left(10)

# Chamar a função de animação


animate()

# Manter a janela aberta
wn.mainloop()
