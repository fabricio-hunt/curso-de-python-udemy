"1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior"

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

if numero1 > numero2:
    print('O maior número é: ', numero1)
elif numero2 > numero1:
    print("O maior número é: ", numero2)
else:
    print("Error")

""" 2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule 
#a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o 
#número é inválido. """

#3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.