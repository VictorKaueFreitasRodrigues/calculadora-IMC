peso = str(input("digite o peso: "))
altura=str(input("digite a altura: "))

imc=float(peso)/(float(altura)*float(altura))
print(type(imc))
print(f"o imc é {round(imc,2)}")


# peso / (altura x altura).