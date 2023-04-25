lista = []

n = int(input("digite o tamanho da lista: "))

for i in range(n):
    num = float(input("digite o valor: "))
    lista.append(num)

soma = sum(lista)

print(f"a soma de {lista} é {soma}!")