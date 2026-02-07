# Exercício 0:** Escreva um programa que use a função `range()` para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.
l = list(range (2,22,2))
print(l)

#Exercício 1:** Crie uma lista chamada numeros que contenha os números inteiros de 1 a 10 e imprima-a na tela.
numeros = list (range(1,11))
print(numeros)

#Exercício 2:** Acesse e imprima o terceiro elemento da lista `numeros`.
numeros = list (range(1,11))
print(numeros[2])

#Exercício 3:** Adicione o número 9 à lista `numeros` e imprima a lista atualizada.
numeros.append(9)
print(numeros)

#Exercício 4:** Remova o número 5 da lista `numeros` e imprima a lista resultante.
numeros.remove(5)
print(numeros)


#Exercício 5:** Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado. """
carros = ['civic', 'argo', 'polo']
ordem = [1,2,3]
print (carros+ordem)

numeros = list(range(2,21,2))
print(numeros)


# 1
numeros = list(range(1,11))
print(numeros) 


# 2
print(numeros[2])


# 3
numeros.append(9)
print(numeros)


# 4
numeros.remove(5)
print(numeros)


# 5
carros = ['jeep','ferrari','fusca']
print(carros , numeros)


carros+=(numeros)
print(carros)