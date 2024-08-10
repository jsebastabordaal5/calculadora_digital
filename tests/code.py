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







