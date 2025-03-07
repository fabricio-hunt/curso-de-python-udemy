"""
Aula sobre Strings em Python
----------------------------

As strings em Python são sequências de caracteres imutáveis.
Podem ser criadas usando aspas simples (' '), duplas (" ") ou triplas (''' ''' ou """ """).
"""

# Criando strings
string_simples = 'Olá, mundo!'
string_dupla = "Python é incrível"
string_tripla = '''Essa é uma string
com múltiplas linhas'''

# Exibindo as strings
print(string_simples)
print(string_dupla)
print(string_tripla)

# Acessando caracteres individuais (indexação)
primeira_letra = string_simples[0]  # Índice 0 -> 'O'
ultima_letra = string_simples[-1]  # Índice -1 -> '!'
print(f"Primeira letra: {primeira_letra}")
print(f"Última letra: {ultima_letra}")

# Fatiamento de strings (slicing)
parte_da_string = string_simples[0:5]  # Pega do índice 0 ao 4 ('Olá, ')
print(f"Parte da string: {parte_da_string}")

# Métodos úteis para manipulação de strings
maiuscula = string_simples.upper()  # Converte para maiúsculas
minuscula = string_dupla.lower()  # Converte para minúsculas
tamanho = len(string_simples)  # Retorna o tamanho da string
substituida = string_simples.replace("mundo", "Python")  # Substitui palavras
palavras = string_dupla.split(" ")  # Divide a string em uma lista de palavras

print(f"Maiúscula: {maiuscula}")
print(f"Minúscula: {minuscula}")
print(f"Tamanho da string: {tamanho}")
print(f"String substituída: {substituida}")
print(f"Lista de palavras: {palavras}")

# Verificando se uma palavra está na string
tem_python = "Python" in string_dupla  # Retorna True se 'Python' estiver na string
print(f"A string contém 'Python'? {tem_python}")

# Concatenando strings
concatenada = string_simples + " " + string_dupla
print(f"String concatenada: {concatenada}")

# Formatando strings
nome = "Davi"
idade = 3
mensagem = f"Meu filho {nome} tem {idade} anos."
print(mensagem)

# Removendo espaços em branco
espacos = "   Texto com espaços    "
sem_espacos = espacos.strip()
print(f"Texto sem espaços: '{sem_espacos}'")
