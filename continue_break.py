
def main():
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        if contador == 322:
            print(contador)
            break
        print(contador)


def busca_letras():
    contador = 0
    texto = input('Escriba un texto ')
    texto = texto.lower()

    for letra in texto:
        if letra == 'a':
            contador += 1
            print(letra)
    print(contador)


if __name__ == '__main__':
    main()
    busca_letras()