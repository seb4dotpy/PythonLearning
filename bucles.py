
def main():
    LIMITE = 1000 #indica el numero maximo que se va a imprimir y operar


    potencia = 0
    acum = 0 #indica el numero acumulado del proceso
    while acum < LIMITE:
        print('2 elevado a ' + str(potencia) + ' es: ' + str(acum))
        acum = 2**potencia    
        potencia +=1
     

def bucle_for():
    
    potencia = 0
    for acum in range(11):
        acum = 2**potencia
        print('2 elevado a ' + str(potencia) + ' es: ' + str(acum))
        potencia +=1


if __name__ == '__main__': #MAIN Y BUCLE_FOR hacen lo mismo, pero con for es mas corto
    main() 
    bucle_for()