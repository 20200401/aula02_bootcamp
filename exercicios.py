import math

#01 - Faça um programa que pe;a dois números inteiros e imprima a divisão inteira do primeiro pelo segundo
try:
    numero_01 = int(input("Inserir um numero inteiro: "))
    numero_02 = int(input("Inserir outro numero inteiro: "))
    resultado = numero_01 // numero_02
    print(resultado)
except ZeroDivisionError as e:
    print(e)

#02 - Escreva um programa que calcule a area do círculo recebendo o raio como entrada
raio_do_circulo = float(input("Digite o raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
print(f"{area_do_circulo:.2f}")

#03 - Faça um programa que peça ao usuario para digitar no formato dd/mm/aaaa e imprima  dia, mes e ano separadamente
data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
lista_de_dia_mes_ano = data_do_usuario.split("/")
print(f"O elemento 1 e o : {lista_de_dia_mes_ano[0]}")
print(f"O elemento 2 e o : {lista_de_dia_mes_ano[1]}")
print(f"O elemento 3 e o : {lista_de_dia_mes_ano[2]}")