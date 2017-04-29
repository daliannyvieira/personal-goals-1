# Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.

a = str(int(2**1000000))
print ('A quantidade de dígitos é: %s' %len(a))
