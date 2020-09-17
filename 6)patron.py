num=int(input("Digite el número que quiere graficar en pantalla: "))
for i in range(num):
    print('*'*i+'*'+' '*(2*num-2*i-2)+'*'*(i+1))
