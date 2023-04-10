NumM, Pist = map(int, input().split())
if 0 < Pist <= 100 and 1 <= NumM <= 100000000:
  while NumM > Pist:
    NumM = NumM - Pist
  if NumM < Pist:
    print(NumM)
  elif NumM == Pist:
    print(0)
