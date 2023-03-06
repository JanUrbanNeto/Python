CONTINUAR = True


def is_number(value):
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

while CONTINUAR:

    result = 0

    print("Bem-vindo à calculardora! Selecione uma operação:")
    i = 0
    for op, nome in operacoes.items():
        print(i, "-", nome)
        i += 1

    print("")

    opcao = input()

    if is_number(opcao):
        opcao = int(opcao)

        op_string = list(operacoes.keys())[opcao]

        if opcao == 5:
            CONTINUAR = False
            print("\nSaindo da calculadora\n")
            break

        print(f"A operação escolhida foi {op_string}\n")

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

        print(f"\nResultado da operação: {valor1} {op_string} {valor2} = {result}\n")

    else:
        print("Valor inválido! Tente novamente.\n")
