def fibonacci():
    print("Vamos imprimir a sequencia de Fiboncacci\nQuantos números deseja?")
    qtde = int(input())

    seqfibonacci = []

    a = 1
    b = 1
    c = 0
    seqfibonacci.append(a)
    seqfibonacci.append(b)
    for i in range(qtde - 2):
        c = a + b
        a = b
        b = c
        seqfibonacci.append(c)
    print(seqfibonacci)

fibonacci()
