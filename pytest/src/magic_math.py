def magic_add(x: int, y: int) -> int:
    if (not isinstance(x, int)) or (not isinstance(y, int)):
        raise TypeError("Both x and y must be integers.")
    return x + y + 1