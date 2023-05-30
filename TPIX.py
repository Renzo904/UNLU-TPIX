def problema1(numeros):
    entrada = input("Ingrese un numero(o salir): ")
    while entrada != "salir":
        if entrada.isdecimal():
            numeros.append(int(entrada))
        entrada = input("Ingrese un numero(o salir): ")
    return numeros

def problema2a(numeros):
    numerosprimos = []
    for numero in numeros:
        esprimo = True

        for j in range(2,int(numero/2)):
            if numero % j == 0:
                esprimo = False
        if numero == 0 or numero == 1 or numero == 4:
            esprimo = False

        if esprimo == True:
            numerosprimos.append(numero)
    return numerosprimos



def problema2b(numeros):
    acc=0
    for numero in numeros:
        acc+=numero
    sumatoria=len(numeros)
    promedio=acc/sumatoria
    return acc,promedio

def problema2c(numeros):
    factoriallista = []
    for numero in numeros:
        factorial = 1
        for i in range(1,numero+1):
            factorial *= i
        factoriallista.append(factorial)
    return factoriallista



print (problema2c([3,2,3,2,4,6,9,7,10,5]))
