def main():
    persona1 = {
        'nombre' : 'Sebastian',
        'apellido': 'Ohberg',
        'edad': 23,
    }
    print(persona1)
    persona1['nombre'] = input('Cambie su nombre')
    print(persona1)


if __name__ == '__main__':
    main()