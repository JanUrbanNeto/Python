
print("digite seu peso:")
peso = input()
peso = float(peso)
print("digite sua altura")
altura = input()
altura = float(altura)
imc = peso/altura ** 2
print("seu IMC é: {}".format("%.2f" % imc))