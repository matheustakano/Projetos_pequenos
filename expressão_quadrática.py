import math

a = 1
b = -1
c = -6

delta = b**2 - 4*a*c
print("O valor do Delta é:",delta)

if delta < 0:
    print("Não temos raízes reais.")
else:
    if delta == 0:
        print("Temos uma raíz real.")
    else:
        if delta > 0:
            print("Temos duas raízes reais.")

raiz1 = -b + math.sqrt(delta) / 2*a 
raiz2 = -b - math.sqrt(delta) / 2*a 

print("A primeira raíz é igual a:",raiz1)
print("A segundo raíz é igual a:",raiz2)

