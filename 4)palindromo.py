text = input('Digite la palabra que desee: ').lower().replace('é','e')
p = (text[::-1])
if p == text:
    print('el texto es palíndromo')

else:
    print('el texto no es palíndromo')
