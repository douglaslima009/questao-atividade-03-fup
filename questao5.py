import math

# Recebe um número do usuário
numero = float(input("Digite um número: "))

# Verifica se o número é positivo ou negativo
if numero >= 0:
    # Calcula a raiz quadrada do número usando a função sqrt() da biblioteca math
    raiz_quadrada = math.sqrt(numero)
    print("A raiz quadrada de", numero, "é", raiz_quadrada)
else:
    # Se o número for negativo, mostra uma mensagem de erro
    print("Número inválido. O número deve ser positivo.")
