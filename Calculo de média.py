min = int(input('Digite qual a média mínima para passar: \n'))
quantnot = int(input('Digite quantas notas que calcular: \n'))

soma = 0
for x in range(1, quantnot+1):
    #soma = a
    a = int(input('Digite sua nota: \n'))
    soma = soma + a

media = soma/quantnot
print ('A soma das notas deram : {}\n' .format(soma))
print ('A media das notas deram : {}\n' .format(media))

if media < min:
    print('Infelizmente você foi reprovado!')
else:
    print('Parabéns você passou!')