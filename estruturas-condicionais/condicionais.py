# condicionais.py

# Estruturas condicionais em Python permitem que o programa tome decisões
# com base em condições. Usamos if, elif e else para isso.

# Exemplo 1: Verificando se um número é positivo

numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero == 0:
    print("O número é zero.")
else:
    print("O número é negativo.")

# Comentário:
# - if: verifica a primeira condição (se o número é maior que 0)
# - elif: verifica outra possibilidade (se é igual a 0)
# - else: se nenhuma das anteriores for verdadeira, executa essa parte

# ----------------------------------------------------------------

# Exemplo 2: Verificando se uma pessoa pode dirigir

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode dirigir.")
else:
    print("Você ainda não pode dirigir.")

# ----------------------------------------------------------------

# Exemplo 3: Verificando par ou ímpar

numero = int(input("Digite outro número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# Comentário:
# - O operador % retorna o resto da divisão
# - Se o resto da divisão por 2 for 0, o número é par

# ----------------------------------------------------------------

# Exemplo 4: Nota de aluno

nota = float(input("Digite a nota do aluno (0 a 10): "))

if nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Em recuperação.")
else:
    print("Reprovado.")

# ----------------------------------------------------------------

# Exemplo 5: Login simples com validação

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == "admin" and senha == "1234":
    print("Login bem-sucedido!")
else:
    print("Usuário ou senha incorretos.")

# Comentário:
# - Operador `and` exige que ambas as condições sejam verdadeiras
