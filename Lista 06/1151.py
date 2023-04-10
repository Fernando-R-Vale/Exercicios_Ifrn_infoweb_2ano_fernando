n = int(input())
soma = 0
lista = []

while soma < n:
  if soma == 0 or soma == 1:
    lista.append(soma)
  if soma > 1:
    a = lista[soma - 2] + lista[soma -1]
    lista.append(a)
  soma = soma + 1
for j in range(0, n):
  lista[j] = str(lista[j])
lista = ' '.join(lista)
print(lista)
