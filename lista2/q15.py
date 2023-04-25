lista = []

n = int(input("digite o tamanho da lista: "))

for i in range(n):
    num = int(input("digite o valor que quer adicionar a lista: "))
    lista.append(num)

n2 = int(input("digite o numero para ver se está na lista: "))
if n2 in lista:
    print(f"o numero {n2} está na lista")
else:
    print(f"o numero {n2} não está")