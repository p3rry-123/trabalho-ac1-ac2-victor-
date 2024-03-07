import math 

def eq_seg_grau(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0 : 
        return None , None
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False
def calcula_salario(valor_hora,num_horas, irpf=0.275):
    salario_bruto = valor_hora * num_horas
    desconto_irpf = salario_bruto * irpf
    salario_liquido = salario_bruto - desconto_irpf 
    return salario_liquido
