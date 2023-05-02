# solicita três números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# ordena os números em ordem crescente
if num1 <= num2 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        medio = num2
        maior = num3
    else:
        medio = num3
        maior = num2
elif num2 <= num1 and num2 <= num3:
    menor = num2
    if num1 <= num3:
        medio = num1
        maior = num3
    else:
        medio = num3
        maior = num1
else:
    menor = num3
    if num1 <= num2:
        medio = num1
        maior = num2
    else:
        medio = num2
        maior = num1

# exibe os números em ordem crescente
print("Os números em ordem crescente são:", menor, medio, maior)
