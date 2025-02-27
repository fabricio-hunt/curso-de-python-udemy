""" Entrada de Dados
    Recebendo dados do usuário
"""
#Todo Dado recebido via input é uma string

#Entrada de Dados
print('Digite seu nome: ')
nome = input()
#Saída de dados
print(f'Seja Bem-vindo(a) {nome}')

#--------------------------------------------------

#Entrada de Dados
print('Digite sua idade: ')
idade = input()
print(f' Olá {nome} Sua idade atual é {idade}')

#casting
print(f' voce nasceu em {2025-int(idade)}')

