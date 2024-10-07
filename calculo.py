#calculadora basica
#opciones que estan disponibles
print ('calculador encendida \n (1): suma \n (2): resta \n (3): multi \n (4): div \n (5): salir ')

while True:
    op=input('operador: \n  ')

    # si op es salir, termina el bucle
    if op in ('salir','5'):
        print('"salida exitosa"')
        break

    #verificacion
    if op not in ('suma','1','resta','2','multi','3','div','4','salir','5'):
        print('especifica los elementos \n(suma/resta/multi/div): ')
        continue

    #los numeros
    n1=float(input('numero: \n '))
    n2=float(input('numero: \n '))

    #logica para las operaciones
    if op in ('suma','1'):
        print(f'la suma de ({n1}) y ({n2}) es ',' \n resultado', n1 + n2)
    elif op in ('resta','2'):
        print(f'la resta de ({n1}) y ({n2}) es ',' \n resultado', n1 - n2)
    elif op in ('multi','3'):
            print(f'la multiplicacion de ({n1}) y ({n2}) es ',' \n resultado', n1 * n2)
    elif op in ('div','4'):
        if n2 != 0:
            print(f'la divicion de ({n1}) y ({n2}) es ',' \n resultado', n1 // n2)
        else:
            print('error no se puede dividir entre 0')
