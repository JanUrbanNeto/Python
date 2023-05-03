x = 1
y = 0

try:
    z = x/y

except ZeroDivisionError:
    print("Erro na Divisão!!")

else:
    print("Deu certo!! {}".format(z))

finally:
    print("“FIM!!”")
