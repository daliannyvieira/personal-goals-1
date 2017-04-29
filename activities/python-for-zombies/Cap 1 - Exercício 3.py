# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

total = (dias * 24 * 60 * 60 ) + (horas * 60 * 60) + (minutos * 60) + segundos # ao invés de usar dias * 24 * 3600, desmembrei)
print ('Convertido em segundos é igual a %10d' %total)
