# Recebe os 4 números do usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))

# Inicializa a variável de soma
soma = 0

# Verifica se cada número é par e, se for, adiciona à soma
if num1 % 2 == 0:
    soma += num1
if num2 % 2 == 0:
    soma += num2
if num3 % 2 == 0:
    soma += num3
if num4 % 2 == 0:
    soma += num4

# Imprime o resultado
print("A soma dos números pares é:", soma)