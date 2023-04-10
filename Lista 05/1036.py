A,B,C = input().split(" ", 3)
A1 = float(A)
C1 = float(C)
B1 = float(B)
calculomucholoco = (B1 ** 2) + (-4 * A1 * C1)
if calculomucholoco <= 0 or A1 == 0:
  print("Impossivel calcular")
else:
  bhascara = (- B1 + calculomucholoco ** 0.5) / (2 * A1)
  bhascara2 = (- B1 - calculomucholoco ** 0.5) / (2 * A1)
  print(f"R1 = {bhascara:.5f}")
  print(f"R2 = {bhascara2:.5f}")
