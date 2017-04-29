# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

distancia = float(input('Digite quantos quilometros foram percorridos: '))
dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))

valor = (dias * 60) + (distancia * 0.15)

print ('O preço a pagar é de R$: %.2f' %valor)
