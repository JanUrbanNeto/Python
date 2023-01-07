continuar = True

def isNumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

operacoes = {
    "+": "Soma",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão",
    "^": "Potenciação",
    "5": "sair"
}

while continuar:
    
    result = 0

    print("Bem-vindo à calculardora! Selecione uma operação:")
    i = 0
    for op, nome in operacoes.items():
        print(i, "-", nome)
        i += 1    

    print("")

    opcao = input()

    if isNumber(opcao):
        
        opcao = int(opcao)

        op_string = list(operacoes.keys())[opcao]

        if opcao == 5:
            continuar = False
            print("\nSaindo da calculadora\n")
            break

        print("A operação escolhida foi {}\n".format(op_string))
        
        print("digite o primeiro valor:")
        valor1 = float(input())

        print("digite o segundo valor:")
        valor2 = float(input())

        if opcao == 0:
            result = valor1 + valor2

        elif opcao == 1:
            result = valor1 - valor2

        elif opcao == 2:
            result = valor1 * valor2

        elif opcao == 3:
            result = valor1 / valor2

        elif opcao == 4:
            result = valor1 ** valor2
        
        print("\nResultado da operação: {} {} {} = {}\n".format(valor1, op_string, valor2 ,result))

    else:
        print("Valor inválido! Tente novamente.\n")       