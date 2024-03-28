a = float(input('Digite um numero'))
b = float(input('Digite um numero'))
c = float(input('Digite um numero'))

if (a + b < c) or (a + c < b) or (b + c < a):
    print ('Não é um Triangulo')
elif ( a == b) and ( a == c):
    print ('O Triangulo é Equilatero')
elif (a==b) or (a==c) or (b==c):
    print ('O Triangulo é Isóceles')
else:
    print ('O Triangulo é Escaleno')