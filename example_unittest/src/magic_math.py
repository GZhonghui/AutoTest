def get_magic_number() -> int:
    return 2

def magic_add(x: int, y: int) -> int:
    if (not isinstance(x, int)) or (not isinstance(y, int)):
        raise TypeError("Both x and y must be integers.")
    return x + y + get_magic_number()