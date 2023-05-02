# Solicita ao usuário os dois números e a operação a ser realizada
num1 = float(input("Digite o primeiro número: "))
op = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

# Realiza a operação escolhida
if op == '+':
    resultado = num1 + num2
elif op == '-':
    resultado = num1 - num2
elif op == '*':
    resultado = num1 * num2
elif op == '/':
    resultado = num1 / num2
else:
    print("Operação inválida.")
    resultado = None

# Mostra o resultado da operação
if resultado is not None:
    print("Resultado: ", resultado)
