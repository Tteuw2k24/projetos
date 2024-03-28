p = float(input('Digite seu peso:'))
a = float(input('Digite sua altura:'))
imc = (p/a**2)
print ("{:.2f}".format(imc))
if imc < 18.5:
    print ('abaixo do peso')
elif imc < 25:
    print ('Peso Normal')
elif  imc < 30:
    print ('Sobrepeso')
else :
    print('Obesidade')