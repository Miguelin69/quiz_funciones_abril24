# ejercicio 2

def ultimo(n):
    resul = n % 10
    return resul

p = int(input("Ingrsa el numero: "))

if ultimo(p) == 4:
    print("El último digito si termina en cuatro ")
else : 
    print("El último digito no termina en cuatro ")