import math

print("Welcome to paint shop of Zé Bonitinho!!!")
print("How much squaremeters do you need to paint?")
m2 = input()
m2 = float(m2)

if m2 < 0:
    m2 = math.fabs(m2)

if m2 < 3:
    total = math.ceil(m2/3)
    print("To paint {} m2, you will need {} can of paint with 1 liter each".format(m2, total))

elif (m2 >= 3) and (m2 < 54):
    total = math.ceil(m2/10.8)
    print("To paint {} m2, you will need {} can of paint with 3.6 liter each".format(m2, total))

else:
    total = math.ceil(m2/54)
    print("To paint {} m2, you will need {} can of paint with 18 liters each".format(m2, total))