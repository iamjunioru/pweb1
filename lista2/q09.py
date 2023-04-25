lista = []

n = int(input("digite o tamanho da lista: "))

for i in range(n):
    num = float(input("digite o valor: "))
    lista.append(num)

media = sum(lista) / n 

print(f"a média é {media}!")
