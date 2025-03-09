# Aula sobre Escopo de Variáveis

# Variáveis Globais e Locais
# ---------------------------
# Em Python, as variáveis podem ser definidas dentro ou fora de funções.
# Isso afeta onde e como elas podem ser acessadas.

# Variável global
nome = "Carlos"  

def exibir_nome():
    # Podemos acessar a variável global dentro da função
    print(f"Nome dentro da função: {nome}")

exibir_nome()
print(f"Nome fora da função: {nome}")

# ---------------------------
# Variáveis Locais
# ---------------------------
# Variáveis criadas dentro de uma função só existem dentro dela.

def saudacao():
    mensagem = "Olá, bem-vindo!"  # Variável local
    print(mensagem)

saudacao()
# print(mensagem)  # Isso geraria um erro, pois 'mensagem' só existe dentro da função.

# ---------------------------
# Modificando Variáveis Globais Dentro de Funções
# ---------------------------
# Para modificar uma variável global dentro de uma função, usamos 'global'

contador = 0  # Variável global

def incrementar():
    global contador  # Indica que estamos usando a variável global
    contador += 1
    print(f"Contador dentro da função: {contador}")

incrementar()
incrementar()
print(f"Contador fora da função: {contador}")

# ---------------------------
# Escopo Aninhado (LEGB - Local, Enclosing, Global, Built-in)
# ---------------------------
# O Python segue a hierarquia de escopos chamada LEGB:
# 1. **Local** – Variáveis dentro da função.
# 2. **Enclosing** – Funções aninhadas (uma função dentro de outra).
# 3. **Global** – Variáveis definidas no nível global.
# 4. **Built-in** – Palavras-chave e funções embutidas do Python.

def externa():
    mensagem = "Olá do escopo externo"  # Variável no escopo externo

    def interna():
        print(mensagem)  # A função interna pode acessar a variável externa

    interna()

externa()

# ---------------------------
# Uso do 'nonlocal' para modificar variáveis em funções aninhadas
# ---------------------------

def contador_externo():
    num = 0  # Variável no escopo externo

    def incrementar():
        nonlocal num  # Permite modificar a variável da função externa
        num += 1
        print(f"Valor dentro da função interna: {num}")

    incrementar()
    incrementar()

contador_externo()
