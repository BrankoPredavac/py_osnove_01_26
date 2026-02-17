class Skijas:
    def __init__(self, ime, prezime, dob, tezina_kg, visina_cm, drzava):
        self.ime = ime
        self.prezime = prezime
        self.dob = dob
        self.tezina_kg = tezina_kg
        self.visina_cm = visina_cm
        self.drzava = drzava

    def skijaj_slalom(self):
        print(f"{self.ime} {self.prezime} skija slalom")

    def skijaj_spust(self):
        print(f"{self.ime} {self.prezime} skija spust")

    def skijaj_veleslaom(self):
        print(f"{self.ime} {self.prezime} skija veleslaom")


janica_kostlic = Skijas(
    ime="Janica",
    prezime="Kostelic",
    dob=42,
    tezina_kg=70.0,
    visina_cm=172,
    drzava="Hrvatska",
)


print(
    f"{janica_kostlic.ime} {janica_kostlic.dob} godine visina {janica_kostlic.visina_cm} cm"
)

# print(janica_kostlic.ljubavnik)
# print(janica_kostlic.ime_brata)

janica_kostlic.skijaj_slalom()
janica_kostlic.skijaj_spust()
janica_kostlic.skijaj_spust()
janica_kostlic.skijaj_spust()
janica_kostlic.skijaj_spust()
janica_kostlic.skijaj_spust()

# janica_kostlic.plivaj()
