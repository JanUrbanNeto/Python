print("digite a nota 01:")
n1 = float(input())

print("digite a nota 02:")
n2 = float(input())

media = (n1 + n2)/2

if media < 7:
    print("reprovado")
elif 10 > media >= 7:
    print("Aprovado")
elif media == 10:
    print("Aprovado com louvor")
