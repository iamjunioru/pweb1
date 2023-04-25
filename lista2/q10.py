lista = []

print("(apenas os numeros pares serão exibidos)")
n = int(input("digite o tamanho da lista: "))

for i in range(n):
    num = int(input("digite o numero: "))
    if num % 2 == 0:
        lista.append(num)

print(f"os números pares são:\n{lista}")