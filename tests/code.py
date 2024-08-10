def suma(num_1: float, num_2: float) -> float:
    return num_1 + num_2


def resta(num_1: float, num_2: float) -> float:
    return num_1 - num_2


def mult(num_1: float, num_2: float) -> float:
    return num_1 * num_2


def div(num_1: float, num_2: float) -> float | str:
    if num_2 != 0:
        return num_1 / num_2
    else:
        return "Error!"


num_1 = float(input("Ingrese el primer número: "))
num_2 = float(input("Ingrese el segundo número: "))
operacion = input("Seleccione la operación que desea realizar: ")

if operacion == 'Suma':
    print(suma(num_1, num_2))
elif operacion == 'Resta':
    print(resta(num_1, num_2))
elif operacion == 'Multiplicación':
    print(mult(num_1, num_2))
elif operacion == 'División':
    print(div(num_1, num_2))

