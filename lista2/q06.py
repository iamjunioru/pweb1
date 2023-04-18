# Escreva um programa em Python que leia um número inteiro e imprima a tabuada desse número (de 1 a 10).

num = int(input("digite o número que deseja para fazer a tabuada dele: "))

for i in range(1, 11):
    resultado = i * num
    print(f"{num} x {i} = {resultado}")