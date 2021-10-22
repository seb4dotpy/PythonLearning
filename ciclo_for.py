
def main():
    palabra = input('Escriba una palabra: ')
    
    for letra in palabra[::-1]: # CON [::-1] se puede imprimir facil al reves, paraescribirlo normalmente solo se elimina
        print(letra)

if __name__ == '__main__':
    main()