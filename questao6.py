nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

if nota1 < 0 or nota1 > 10:
    print("Nota inválida!")
elif nota2 < 0 or nota2 > 10:
    print("Nota inválida!")
elif nota3 < 0 or nota3 > 10:
    print("Nota inválida!")
else:
    media = (nota1 + nota2 + nota3) / 3
    print("A média das notas é: {:.2f}".format(media))
