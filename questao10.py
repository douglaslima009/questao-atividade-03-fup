# solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# exibe as opções de operação disponíveis
print("Escolha uma operação:")
print("1 - Média entre os números digitados")
print("2 - Diferença do maior pelo menor")
print("3 - Produto entre os números digitados")
print("4 - Divisão do primeiro pelo segundo")

# solicita a escolha do usuário
opcao = int(input("Opção escolhida: "))

# realiza a operação escolhida pelo usuário
if opcao == 1:
    media = (num1 + num2) / 2
    print("A média entre os números é:", media)
elif opcao == 2:
    diferenca = abs(num1 - num2)
    print("A diferença entre os números é:", diferenca)
elif opcao == 3:
    produto = num1 * num2
    print("O produto entre os números é:", produto)
elif opcao == 4:
    if num2 == 0:
        print("Não é possível dividir por zero.")
    else:
        divisao = num1 / num2
        print("A divisão do primeiro pelo segundo é:", divisao)
else:
    print("Opção inválida.")
