numeros = []

print("Comparação de 3 números")

for i in range(3):
    print(F"Digite o {i+1}º número:")
    numero = int(input())
    numeros.append(numero)

print(F"O maior número é {max(numeros)} e o menor éffffffffff {min(numeros)}.")
