ime_prezime: str = "Marko Maric"
oib: str = "4314325252"
email: str = "marko.maric@algebra.hr"
broj_telefona: str = "098/787-1234"
prosjecna_ocjena: float = 4.2
godina_upisa: int = 2005
naziv_studija: str = "PMF Biologija"
naziv_sveucilista: str = "Zagrebacko sveuciliste"


print(f"Ime i prezime: {ime_prezime}")
print(f"OIB: {oib}")
print(f"E-Mail: {email}")
print(f"Broj mobitela: {broj_telefona}")
print(f"Godina upisa studija: {godina_upisa}")
print(f"Naziv studija: {naziv_studija}")
print(f"Naziv sveucilista: {naziv_sveucilista}")


print("\n")

print(
    f"Ime i prezime: {ime_prezime}\nOIB: {oib}\nE-Mail: {email}\nBroj mobitela: {broj_telefona}\nGodina upisa studija: {godina_upisa}\nNaziv studija: {naziv_studija}\nNaziv sveucilista: {naziv_sveucilista}"
)

print("\n")

print(
    f"Ime i prezime: {ime_prezime}",
    f"OIB: {oib}",
    f"E-Mail: {email}",
    f"Broj mobitela: {broj_telefona}",
    f"Godina upisa studija: {godina_upisa}",
    f"Naziv studija: {naziv_studija}",
    f"Naziv sveucilista: {naziv_sveucilista}",
    sep="\n",
)
