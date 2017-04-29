# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

mercadoria = float(input('Digite o valor da mercadoria: '))
desconto = float(input('Digite a porcentagem de desconto: '))
totalDesconto = mercadoria * (desconto / 100)
totalMercadoria = mercadoria - totalDesconto

print ('Você pagará R$ %.2f' %totalMercadoria)
print( 'Seu desconto foi de R$ %.2f' %totalDesconto)
