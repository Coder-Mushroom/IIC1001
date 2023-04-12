if __name__ == '__main__':
    print('¡Bienvenido a Chequeador de Paridad! (^o^)')
    user_input = input(
        'Ingrese un \033[1;34;40mnúmero entero positivo\033[0m: ')
    if user_input.isnumeric():
        user_number = int(user_input)
        parity = '\033[1;34;40mPar\033[0m' if user_number % 2 == 0 else '\033[1;34;40mImpar\033[0m'
        print(
            f'El número {user_number} es {parity}\n¡Gracias por usar el programa! ^^')
    else:
        print('\033[1;31;40mError:\033[0m El valor ingresado no es válido')
