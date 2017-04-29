# Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input('Digite a distância que irá percorrer (km): '))
velocidademedia = float(input('Digite a velocidade que deseja pra viagem (km/h): '))

tempo = distancia / velocidademedia


print ('Sua viagem vai demorar: %.1f hora(s)' %tempo)