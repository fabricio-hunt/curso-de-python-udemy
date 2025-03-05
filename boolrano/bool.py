"""
Aula: Trabalhando com Booleanos em Python no VSCode

Nesta aula, vamos explorar o tipo de dado booleano (`bool`) no Python,
como usá-lo em expressões lógicas e sua importância na programação.
"""

# Definição de valores booleanos
verdadeiro = True  # Representa o valor verdadeiro
falso = False  # Representa o valor falso

print("Valor de verdadeiro:", verdadeiro)
print("Valor de falso:", falso)

# Tipo de dado booleano
print("Tipo de verdadeiro:", type(verdadeiro))  # Saída: <class 'bool'>
print("Tipo de falso:", type(falso))  # Saída: <class 'bool'>

"""
Valores que Python considera como False:
 - 0 (zero)
 - "" (string vazia)
 - [] (lista vazia)
 - () (tupla vazia)
 - {} (dicionário vazio)
 - None (valor nulo)
"""

print("0 é falso?", bool(0))  # False
print("Lista vazia é falsa?", bool([]))  # False
print("String não vazia é verdadeira?", bool("Python"))  # True

# Operadores lógicos
# AND (e), OR (ou) e NOT (negação)

a = True
b = False

print("a AND b:", a and b)  # False
print("a OR b:", a or b)  # True
print("NOT a:", not a)  # False

# Comparações retornam booleanos
x = 10
y = 20

print("x > y:", x > y)  # False
print("x < y:", x < y)  # True
print("x == y:", x == y)  # False
print("x != y:", x != y)  # True

"""
Dicas para usar booleanos no código:
- Use expressões booleanas para controle de fluxo (if, while, etc.).
- Evite comparações desnecessárias, por exemplo:
  ❌ if x == True:  ✅ if x:
  ❌ if x == False: ✅ if not x:
- Use `bool(valor)` para converter outros tipos para booleanos quando necessário.
"""
