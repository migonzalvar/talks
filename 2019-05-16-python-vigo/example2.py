from random import randint

def dice():
    return randint(1,6)

dice()

[(x := dice(), f"Salió un {x}") for _ in range(10)]
