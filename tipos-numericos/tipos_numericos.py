# Aula sobre Tipos Numéricos em Python

# Inteiros (int): números sem parte decimal
inteiro = 10
print(f'Inteiro: {inteiro} | Tipo: {type(inteiro)}')

# Ponto flutuante (float): números com parte decimal
flutuante = 10.5
print(f'Ponto Flutuante: {flutuante} | Tipo: {type(flutuante)}')

# Números complexos (complex): possuem parte real e imaginária
complexo = 3 + 4j
print(f'Complexo: {complexo} | Tipo: {type(complexo)}')

# Operações básicas entre números
soma = inteiro + flutuante  # Adição
subtracao = inteiro - flutuante  # Subtração
multiplicacao = inteiro * flutuante  # Multiplicação
divisao = inteiro / flutuante  # Divisão (sempre retorna float)

print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Divisão: {divisao}')

# Divisão inteira (//): retorna o quociente sem o resto
divisao_inteira = inteiro // 3
print(f'Divisão Inteira: {divisao_inteira}')

# Módulo (%): retorna o resto da divisão
resto = inteiro % 3
print(f'Resto da Divisão: {resto}')

# Exponenciação (**): potência de um número
potencia = inteiro ** 2
print(f'Potência: {potencia}')

# Conversão entre tipos numéricos
float_para_int = int(flutuante)  # Converte float para int (trunca a parte decimal)
int_para_float = float(inteiro)  # Converte int para float

print(f'Float para Int: {float_para_int}')
print(f'Int para Float: {int_para_float}')

# Uso da função round() para arredondamento
arredondado = round(flutuante)
print(f'Arredondamento de {flutuante}: {arredondado}')

# Números grandes e notação científica
numero_grande = 1e6  # 1 milhão (1 * 10^6)
print(f'Número grande: {numero_grande}')

# Verificação de tipos
print(f'É inteiro? {isinstance(inteiro, int)}')
print(f'É float? {isinstance(flutuante, float)}')
print(f'É complexo? {isinstance(complexo, complex)}')
