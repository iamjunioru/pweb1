lista = []

n = int(input("digite o tamanho da lista: "))

for i in range(n):
    num = int(input("digite o valor: "))
    lista.append(num)

lista.sort()
print(lista)