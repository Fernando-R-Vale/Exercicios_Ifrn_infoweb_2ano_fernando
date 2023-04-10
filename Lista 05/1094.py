Repeat = int(input())
Contc = 0 
conts = 0
contR = 0
total = 0
for i in range(Repeat):
    Numb, quale = input().split()
    Numb = int(Numb)
    if quale == 'C':
        Contc += Numb
    elif quale == 'R':
        contR += Numb
    elif quale == 'S':
        conts += Numb
    total += Numb
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {Contc}")
print(f"Total de ratos: {contR}")
print(f"Total de sapos: {conts}")
print(f'Percentual de coelhos: {(Contc*100)/total:.2f} %')
print(f'Percentual de ratos: {(contR*100)/total:.2f} %')
print(f"Percentual de sapos: {(conts/total)*100:.2f} %")
