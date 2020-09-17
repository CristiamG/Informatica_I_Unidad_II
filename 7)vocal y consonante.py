l = input("Digite un caracter válido del alfabeto ").lower()

if l in ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú'):
	print("el caracter %s es una vocal." % l)
elif l in ('y','.',',','-','_',',','}','{','[',']','+','´','*','¨','¿','¡',"'",'?','=',')','(','/','&','%','$','#','"','!','°','0','1','2','3','4','5','6','7','8','9'):
	print("El caracter que acabo de digitar no corresponde a una letra")
else:
	print("el caracter %s es una consonante" % l)
