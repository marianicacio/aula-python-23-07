class cores:
    vermelho = '\033[31m'
    verde = '\033[32m'
    linha = '\033[4m'
    marcação = '\033[103m'
    resetar = '\033[0m'

print (cores.vermelho + 'Texto' + cores.resetar)
print (cores.verde + 'Texto' + cores.resetar)
print (cores.linha + 'Texto' + cores.resetar)
print (" ")
print (cores.marcação + 'Texto' + cores.resetar)


numero = int(input("Digite um número de 1 a 10: "))

if numero <= 10 and numero >=1 :
    print (cores.verde + 'Número válido' + cores.resetar)
else: 
    print (cores.vermelho + 'Número inválido' + cores.resetar)