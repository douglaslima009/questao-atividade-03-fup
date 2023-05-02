salario = float(input("Digite o salário do trabalhador: "))
prestacao = float(input("Digite o valor da prestação do empréstimo: "))

limite = salario * 0.2

if prestacao > limite:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")