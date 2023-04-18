# Escreva um programa em Python que leia dois números inteiros e imprima o maior deles.

num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))

if num1 > num2:
    print(f"o número maior é {num1}.")
else:
    print(f"o número maior é {num2}.")