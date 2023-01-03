print("qual valor do seu salário por hora?")
salario_hora = float(input())
print("quantas horas trabalhou neste mês?")
horas_trabalhadas = float(input())
salario_bruto = salario_hora * horas_trabalhadas
inss = salario_bruto * 0.08
ir = salario_bruto * 0.11
sindicato = salario_bruto *0.05
salario_liquido = salario_bruto - (inss + ir + sindicato)
print("esse mes vc ganhou R$ {} de salário bruto, pagou R$ {} ao INSS, R$ {} ao imposto de renda e R$ {} ao sindicato, ficando seu salário líquido R$ {}".format("%.2f" % salario_bruto, "%.2f" % inss, "%.2f" % ir, "%.2f" % sindicato, "%.2f" % salario_liquido))