CONSTANTE_BONUS = 1000

#1) Solicita ao usuario que digite seu nome
nome_usuario = input("Digite seu nome: ")

if nome_usuario.isdigit():
    print("Voce digitou seu nome errado")
    exit()
elif len(nome_usuario) == 0:
    print("Voce nao digitou nada")
    exit()
elif nome_usuario.isspace():
    print("Voce digitou so espaco")
    exit()   

#2) Solicita ao usuario que digite o valor do seu salario