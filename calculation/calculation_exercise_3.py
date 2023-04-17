def delta_of_quadratic_equation(a: int, b: int, c: int):
    # quadratic eq = ax ** 2 + bx + c
    # delta = b ** 2 - 4ac
    delta = b ** 2 - (4 * a * c)
    return delta