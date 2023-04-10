Cont = int(input())
for i in range(0,Cont):
    R1, R2 = map(int, input().split(" "))
    if R2 == 0:
        print("divisao impossivel")
    else:
        print(R1 / R2)
