#Faça um programa que leia uma frase pelo teclado e mostre: > Quantas vezes aparece a letra "A"./ >Em que posição ela aparece a primeira vez./ >Em que posição ela aparece a última vez. (o primeiro "A" ta na posição e o ultimo na posição tal.)
frase = str(input('Digite uma frase: ')).strip()
print('A letra "A" aparece {} vezes'.format(frase.upper().count('A')))
print('O primeiro "A" ta na posição: {}'.format(frase.upper().find('A')+1))
print('O ultimo "A" ta na posição: {}'.format((frase.upper().rfind)('A')+1))
