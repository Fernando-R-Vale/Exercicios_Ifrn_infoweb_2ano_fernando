A,B = input().split(" ")
A1 = int(A)
B1 = int(B)
Verificador_iniucial = int(B1 / A1)
Verificaor_final = B1 - (Verificador_iniucial * A1)
verificador_iniucial = int(A1 / B1)
verificaor_final = A1 - (verificador_iniucial * B1)
if Verificaor_final == 0 or verificaor_final == 0:
  print("Sao Multiplos")
else:
  print("Nao sao Multiplos")
