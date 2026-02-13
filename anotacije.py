# int_varijable: int = 100
# bool_varijable: bool = 100
# str_varijable: str = 100
# float_varijable: float = 100

# prvi_broj: int = 355235
# drugi_broj = 52435243
# rezultat = prvi_broj + drugi_broj


def zbrajnaje(prvi_broj: int, drugi_broj: int) -> int:
    """Funkciaj zbrajanjaa dva broja

    Args:
        prvi_broj (int): prvi broj
        drugi_broj (int): drugi broj

    Returns:
        int: rezultat zbrajnja
    """
    print(type(prvi_broj))
    return prvi_broj + drugi_broj


print(zbrajnaje(prvi_broj=10, drugi_broj=30), end="\n\n")
print(zbrajnaje(prvi_broj="Idemo ", drugi_broj=" dalje"), end="\n\n")
print(zbrajnaje(prvi_broj=[636, 99, 88], drugi_broj=[77, 44, 11]), end="\n\n")
print(zbrajnaje(prvi_broj=True, drugi_broj=False), end="\n\n")


print("Gotovo")
