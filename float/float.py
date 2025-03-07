# Aula sobre o tipo float em Python
# Um float (ponto flutuante) é um número que pode conter casas decimais.

# Declarando variáveis do tipo float
numero1 = 10.5  # Um número decimal
numero2 = -3.14  # Um número negativo
numero3 = 2.0  # Mesmo sem casas decimais, é considerado float

# Exibindo os valores e seus tipos
print("Número 1:", numero1, "- Tipo:", type(numero1))
print("Número 2:", numero2, "- Tipo:", type(numero2))
print("Número 3:", numero3, "- Tipo:", type(numero3))

# Operações com floats
soma = numero1 + numero2  # Soma de floats
subtracao = numero1 - numero2  # Subtração
multiplicacao = numero1 * numero3  # Multiplicação
divisao = numero1 / numero3  # Divisão
exponenciacao = numero1 ** 2  # Potência

# Exibindo os resultados
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Exponenciação:", exponenciacao)

# Conversão para float
inteiro = 5  # Um número inteiro
convertido = float(inteiro)  # Convertendo para float
print("Número inteiro convertido para float:", convertido, "- Tipo:", type(convertido))

# Precisão de ponto flutuante (problema comum em cálculos)
num_a = 0.1 + 0.2  # O resultado esperado seria 0.3, mas...
print("0.1 + 0.2 =", num_a)  # Pode exibir um valor impreciso devido à forma como os floats são armazenados

# Arredondamento de float
arredondado = round(num_a, 2)  # Arredonda para 2 casas decimais
print("Arredondado para 2 casas decimais:", arredondado)

# Comparação segura entre floats (evitando problemas de precisão)
import math
print("Os valores são aproximadamente iguais?", math.isclose(num_a, 0.3, rel_tol=1e-9))  # Usa uma tolerância relativa para comparação

# Trabalhando com números grandes e pequenos
numero_grande = 1.5e6  # Equivalente a 1.500.000 (1.5 * 10^6)
numero_pequeno = 2.5e-4  # Equivalente a 0.00025 (2.5 * 10^-4)
print("Número grande:", numero_grande)
print("Número pequeno:", numero_pequeno)
