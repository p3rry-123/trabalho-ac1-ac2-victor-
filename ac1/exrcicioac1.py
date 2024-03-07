import math
def calcular_raizes(a,b,c):
    delta = b**2 - 4*a*c
    if delta  > 0 :
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b + math.sqrt(delta)) / (2*a)
        return raiz1, raiz2
    elif delta == 0:
        raiz = -b / (2*a)
        return raiz, 
    else:    
        return None

# 
a = 10
b = -8
c = 5

raizes = calcular_raizes(a, b, c)
if raizes:
    if len(raizes) == 2:
        print("As raízes são:", raizes[0], "e", raizes[1])
    else:
        print("A raiz é:", raizes[0])
else:
    print("Não há raízes reais.")


ano=int(input("digite o ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0 ):
    print (ano, "é ano bissexto.")
else:
    print (ano, "não é ano bissexto.")

