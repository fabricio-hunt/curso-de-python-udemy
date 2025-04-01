# ------------------------------
# Aula de Operadores Lógicos em Python
# and / or / not / is
# ------------------------------

# 1. Operador AND (E)
print("=== Operador AND ===")
a = True
b = False
print(a and b)  # False: os dois precisam ser True

# Exemplo prático:
idade = 25
tem_carteira = True
if idade >= 18 and tem_carteira:
    print("Pode dirigir.")
else:
    print("Não pode dirigir.")

# ------------------------------

# 2. Operador OR (OU)
print("\n=== Operador OR ===")
a = True
b = False
print(a or b)  # True: apenas um precisa ser True

# Exemplo prático:
tem_dinheiro = False
tem_cartao = True
if tem_dinheiro or tem_cartao:
    print("Compra aprovada.")
else:
    print("Compra negada.")

# ------------------------------

# 3. Operador NOT (NÃO)
print("\n=== Operador NOT ===")
a = True
print(not a)  # False: inverte o valor booleano

# Exemplo prático:
chovendo = False
if not chovendo:
    print("Pode sair sem guarda-chuva.")
else:
    print("Leve o guarda-chuva!")

# ------------------------------

# 4. Operador IS (É)
print("\n=== Operador IS ===")
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)  # True: x e y apontam para o mesmo objeto na memória
print(x is z)  # False: mesmo conteúdo, mas objetos diferentes

# Exemplo prático:
a = None
if a is None:
    print("A variável está vazia (None).")

# Comparação alternativa:
if a == None:  # Funciona, mas o uso de "is" é mais recomendado com None
    print("Comparando com == também funciona, mas prefira 'is'.")

# ------------------------------

# Fim da aula
print("\nFim da aula!")
