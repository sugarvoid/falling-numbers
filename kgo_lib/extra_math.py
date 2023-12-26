# extra_math.py 0.1.0

def clamp(n: int|float, min: int|float, max: int|float) -> int|float:
    if n < min:
        return min
    elif n > max:
        return max
    else:
        return n