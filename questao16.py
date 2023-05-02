def verificar_triangulo(A, B, C):
    if A >= B + C or B >= A + C or C >= A + B:
        # Não é possível formar um triângulo com esses valores
        return "Não é um triângulo"
    elif A == B and B == C:
        # Triângulo equilátero
        return "Triângulo equilátero"
    elif A == B or A == C or B == C:
        # Triângulo isósceles
        return "Triângulo isósceles"
    else:
        # Triângulo escaleno
        return "Triângulo escaleno"


# Testes

print(verificar_triangulo(3, 4, 5))
print(verificar_triangulo(3, 3, 3))
print(verificar_triangulo(4, 4, 5))