ano = int(input("Digite o ano: "))

if ano % 400 == 0:
    bissexto = True
elif ano % 4 == 0 and ano % 100 != 0:
    bissexto = True
else:
    bissexto = False

if bissexto:
    print(ano, "é um ano bissexto")
else:
    print(ano, "não é um ano bissexto")
