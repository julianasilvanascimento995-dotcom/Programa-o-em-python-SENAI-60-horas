import random

aleatorio = random.randint(1,10)
chute = int(input('chute um numero:'))

if aleatorio == chute:
    print ('boa😉')
    print ('não foi dessa vez😭')

else:
    print ('sinto muito, não foi dessa vez😶‍🌫️')
    print ('o numero é:', aleatorio)