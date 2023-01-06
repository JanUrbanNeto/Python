numeros = []

print("Comparação de 3 números")

for i in range(3):
    print("Digite o {}º número:".format(i+1))
    numero = int(input())
    numeros.append(numero)

print("O maior número digitado foi {} e o menor foi {}.".format(max(numeros), min(numeros)))