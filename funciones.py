# funciones en python

def imprimir_mensaje():
     print('Mensaje generico para aprender funciones :D')

imprimir_mensaje()

# Parametros en funciones
def conversacion(mensaje):
    print('Hola, como estas?')
    print(mensaje)
    print('Adios')

opcion = input('Por favor elige una opcion ')

if opcion == '1':
    conversacion('Elegiste la opcion 1')
elif opcion == '2' :
    conversacion('Elegiste la opcion 2')
elif opcion == '3':
    conversacion('Elegiste la opcion 3')
else:
    print('Elige una opcion valida')

# regresar un resultado con una funcion
def suma(a, b):
    print('Se suman dos numeros')
    resultado = a + b 
    return resultado

sumatoria = suma(1,4)
print(sumatoria)

