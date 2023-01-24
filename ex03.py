print("Digite seu e-mail completo:")
email = input()
lista = email.split("@")
print("Seu domínio de e-mail: {}".format(lista[1]))
