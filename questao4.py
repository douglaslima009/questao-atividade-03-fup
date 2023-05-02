# Recebe os 3 valores do usuário
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

# Inicializa a variável de máximo com o primeiro valor
maximo = valor1

# Verifica se o segundo valor é maior que o máximo atual
if valor2 > maximo:
    maximo = valor2

# Verifica se o terceiro valor é maior que o máximo atual
if valor3 > maximo:
    maximo = valor3

# Imprime o resultado
print("O maior valor é:", maximo)
