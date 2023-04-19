import math

def geometric_mean(numbers: list) -> float:
    root = len(numbers)

    return round(math.prod(numbers) ** (1/root), 2)