lista = []

print("(apenas os numeros impares serão exibidos)")
n = int(input("digite o tamanho da lista: "))

for i in range(n):
    num = int(input("digite o numero: "))
    if num % 2 == 1:
        lista.append(num)

print(f"os números impares são:\n{lista}")