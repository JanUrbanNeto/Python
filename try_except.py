x = [1, 2, 3]
y = 1

try:
    # x + y
    z = y + 1
except Exception as e:
    print("erro: {}".format(e))
finally:
    print("esse finally vai executar sempre")
