num=int(input("Digite el número que quiere graficar en pantalla: "))
for i in range(1,num+1):
    print('*'*i+' '*(2*num-2*i)+'*'*i)
