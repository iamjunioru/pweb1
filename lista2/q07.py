n = int(input('digite o número pra sequencia fibonacci: '))

n1 = 1
n2 = 1
count = 0

lista = [0,1,1]

for vic in range(0, n):
    count = n1 + n2
    n1 = count
    n2 = (count - n2)
    lista.append(count)

    print(lista)