import math

print("Welcome to paint shop of Zé Bonitinho!!!")
print("How much squaremeters do you need to paint?")
m2 = input()
m2 = float(m2)
total = math.ceil(m2/54)
print("To paint {} m2, you will need {} can of paint with 18 liters".format(m2, total))