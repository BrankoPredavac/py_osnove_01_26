# broj_godina_str = input("Dragi korisnice, koliko imas godina >").strip().lower()

# broj_godina = int(broj_godina_str)

broj_godina = 22

if broj_godina < 18:
    print("Ti si maloljetan")
elif broj_godina >= 18 and broj_godina < 30:
    print("Ti si mlada osoba")
elif broj_godina >= 30 and broj_godina < 50:
    print("Ti si u zlatnim godinama")
elif broj_godina >= 18 and broj_godina < 25:
    print("Ti si student")
elif broj_godina >= 50 and broj_godina < 65:
    print("Ti si godinama pred mirovinu")
elif broj_godina >= 65:
    print("Ti si u mirovini")
