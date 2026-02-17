print("Pocetak")

korisnik_ulogiran = True
da_li_je_administrator = False


def funkcije(korisnik_ulogiran, da_li_je_administrator):
    if korisnik_ulogiran and da_li_je_administrator:
        print("Dobro dosao Admine")
        return

    if korisnik_ulogiran and not da_li_je_administrator:
        print("Dobro dosao korisnice")
        return

    print("Nekakv obavijest")
    return


print("Gotovo")
