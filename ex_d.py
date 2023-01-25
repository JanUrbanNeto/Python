def fibonacci(n):
    print(1)
    anterior = 0
    proximo = 1
    for i in range(n-1):
        soma = anterior + proximo
        anterior = proximo
        proximo = soma
        print(soma)

numero = int(input("digite um número:"))
fibonacci(numero)
