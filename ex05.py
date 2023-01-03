print("qual valor do seu salário por hora?")
salario_hora = float(input())
print("quantas horas trabalhou neste mês?")
horas_trabalhadas = float(input())
salario_bruto = salario_hora * horas_trabalhadas
inss = salario_bruto * 0.08
ir = salario_bruto * 0.11
sindicato = salario_bruto *0.05
salario_liquido = salario_bruto - (inss + ir + sindicato)
print("esse mes vc ganhou R$ {} de salário bruto.".format("%.2f" % salario_bruto))
print("pagou R$ {} ao INSS.".format("%.2f" % inss))
print("pagou R$ {} ao imposto de renda.".format("%.2f" % ir))
print("pagou R$ {} ao sindicato.".format("%.2f" % sindicato))
print("seu salário líquido R$ {}".format("%.2f" % salario_liquido))