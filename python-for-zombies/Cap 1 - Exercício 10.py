# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarro = int(input('Cigarros por dia: '))
anos = int(input('Anos fumados '))

soma = cigarro *(anos * 365) # resultado em dias da quantidade de vida perdida
dias_perdidos = soma / 144  # fazer regra de 3, se a cada 10 min 1 cigarro , 1 dia tem 1440 minutos, então seria 144 cigarros


print ('Você já perdeu %.2f dias de vida' %dias_perdidos)