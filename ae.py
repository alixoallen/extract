valores=[]

while True:
    valores.append(int(input('digite um valor : ')))
    resp=str(input('quer continuar ? [S/N] ')).upper().strip()
    if resp in "Nn":
        break
print(f'você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'os valores em ordem decrescente são : {valores}')
if 5 in valores:
    print('o numero 5 está na lista ')
else:
    print('o numero 5 não esta na lista ')


