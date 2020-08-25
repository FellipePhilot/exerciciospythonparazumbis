
min = float(input("Digite a quantidade de minutos: "))

if min <= 200:
    conta = min * 0.20
    print(f"Sua conta esta no valor de R$ {conta:.2f}")
elif min > 200 <= 400:
    conta = min * 0.18
    print(f"Sua conta esta no valor de R$ {conta:.2f}")
else:
    conta = min * 0.15
    print(f"Sua conta esta no valor de R$ {conta:.2f}")