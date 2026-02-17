tip_kave = (
    input(
        "Zelis li (odaberi broj):\n\t1. Espresso\n\t2. Cappucino\n\t3. Decaffe\n\t4. Nista\n>"
    )
    .strip()
    .lower()
)
# "  Y  "
# "Y" nakon strip
# "y" nakon lower


if tip_kave == "1":
    print("Priprema esspresso ...")
    print("Esspresso gotov ...")
    print("Posluzujem esprersso ...")
elif tip_kave == "2":
    print("Priprema cappucino ...")
    print("Cappucino gotov ...")
    print("Posluzujem cappucino ...")
elif tip_kave == "3":
    print("Priprema Decaffe ...")
    print("Decaffe gotov ...")
    print("Posluzujem Decaffe ...")
elif tip_kave == "4":
    print("Ne radim nista")
else:
    print("Odabrao si broj koji ne postoji")

print("Gotovo")
