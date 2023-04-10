A1 = int(input())
A2 = int(input())
A3 = int(input())
Andar_3 = (A2 * 2) + (A1 * 4)
Andar_2 = (A3 * 2) + (A1 * 2)
Andar_1 = (A2 * 2) + (A3 * 4)
Maior = 0
if Andar_3 <= Andar_2:
   Maior = Andar_3
else:
    Maior = Andar_2
if Maior <= Andar_1:
    print(Maior)
else:
    print(Andar_1)
