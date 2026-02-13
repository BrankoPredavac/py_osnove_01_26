# uzmete od korisnika Ime
# Koliko godina
# koji mu je najdrazi film
# koju ocjenu bi mu dao

ime_korsnika = input("Dragi korisnice unesite svoje ime> ")
dob_korisnika = input("Dragi korisnice koliko godina imas> ")
najdrazi_film = input("Dragi korisnice koji ti je najdrazi film> ")
ocjena_za_najdrazi_film = input(
    "Dragi korisnice koju ocjenu bi dao svom najdrazem filmu> "
)

print(end="\n\n\n")
print("Ime:", ime_korsnika)
print("Dob:", dob_korisnika)
print("Najdrazi film:", najdrazi_film)
print("Korisnikova ocjena za", najdrazi_film, "je", ocjena_za_najdrazi_film)

ispis_ocjena = (
    "Korisnikova ocjena za " + najdrazi_film + " je " + ocjena_za_najdrazi_film
)
print(ispis_ocjena)

# Ime: korisnikovo Ime
# Dob: korsinikove godine
# Najdrazi film: naziv filma
# Korisnikova ocjena za <naziv filma> je <ocjena korisnika>
