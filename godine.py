broj_godina_str = input("Dragi korisnice, koliko imas godina >").strip().lower()

broj_godina = int(broj_godina_str)


if broj_godina < 18:
    print("Ti si maloljetan")
elif broj_godina >= 18 and broj_godina < 30:
    print("Ti si malada osoba")
elif broj_godina >= 30 and broj_godina < 50:
    print("Ti si u zlatnim godinama")
elif broj_godina >= 50 and broj_godina < 65:
    print("Ti si godinama pred mirovinu")
elif broj_godina >= 65:
    print("Ti si u mirovini")


# if broj_godina < 18:
#     print("Ti si maloljetan")
# elif broj_godina < 30:
#     print("Ti si malada osoba")
# elif broj_godina < 50:
#     print("Ti si u zlatnim godinama")
# elif broj_godina < 65:
#     print("Ti si godinama pred mirovinu")
# else:
#     print("Ti si u mirovini")


# if broj_godina < 18:
#     print("Ti si maloljetan")
# elif broj_godina < 50:
#     print("Ti si u zlatnim godinama")
# elif broj_godina < 30:
#     print("Ti si malada osoba")
# elif broj_godina < 65:
#     print("Ti si godinama pred mirovinu")
# else:
#     print("Ti si u mirovini")


if broj_godina < 30:
    print("Ti si malada osoba")
elif broj_godina < 18:
    # DEAD CODE, kod koji se ni u jednom slucaju nece izvrsit
    print("Ti si maloljetan")
elif broj_godina < 50:
    print("Ti si u zlatnim godinama")
elif broj_godina < 65:
    print("Ti si godinama pred mirovinu")
else:
    print("Ti si u mirovini")


def funckija(broj_godina):
    if broj_godina < 30:
        print("Ti si malada osoba")
        return

    if broj_godina < 18:
        # DEAD CODE, kod koji se ni u jednom slucaju nece izvrsit
        print("Ti si maloljetan")
        return

    if broj_godina < 50:
        print("Ti si u zlatnim godinama")
        return

    if broj_godina < 65:
        print("Ti si godinama pred mirovinu")
        return

    print("Ti si u mirovini")
    return
