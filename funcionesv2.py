print("Mas sobre funciones")
# Aqui se escriben la funciones
def suma_ab(a,b):
    s=a+b
    return s

def res_ab(a1,b2):
    s1=a1-b2
    return s1

def multi_ab(a3,b4):
    s2=a3*b4
    return s2

def div_ab(a5,b6):
    s3=a5/b6
    return s3

# LLamadas a funciones
print("Calculando suma:")
n1=int(input("Ingresa el primer numero "))
n2=int(input("Ingresa el segundo numero "))
suma=suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es: {suma}")
#----------------------------------------------------
print("")
print("Calculando resta")
num1=int(input("Ingresa el primer numero "))
num2=int(input("Ingresa el segundo numero "))
resta=res_ab(num1,num2)
print(f"La resta de {num1} - {num2} es: {resta}")
#----------------------------------------------------
print("")
print("Calculando Multiplicacion")
num3=int(input("Ingresa el primer numero "))
num4=int(input("Ingresa el segundo numero "))
multiplicacion=multi_ab(num3,num4)
print(f"La multiplicacion de {num3} * {num4} es: {multiplicacion}")
#----------------------------------------------------
print("")
print("Calculando Division")
num5=int(input("Ingresa el primer numero "))
num6=int(input("Ingresa el segundo numero "))
division=div_ab(num5,num6)
print(f"La Division de {num5} / {num6} es: {division}")
