a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("Não é equação do 2º grau.")
else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Não existe raiz real.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Raiz única: {x}")
    else:
        x1 = (-b + (delta)**0.5) / (2*a)
        x2 = (-b - (delta)**0.5) / (2*a)
        print(f"Raízes reais: {x1} e {x2}")
