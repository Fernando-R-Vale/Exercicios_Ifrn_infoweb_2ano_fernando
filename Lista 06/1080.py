COntador = 0
B = 0
for i in range(100):
  A = int(input())
  B = B + 1
  if COntador < A:
    COntador = A
    Valusupreme = B
  else:
    COntador = COntador
print(COntador)  
print(Valusupreme)
