# ime proizvoda
# kolicinu
# cijena 1 kom bez pdv
# pdv na proizvod

# ===========================================================================================
# | Ime proizvoda | količina | cijena 1 kom bez PDV (EUR)  | PDV % | Ukupna cijena s PDV (EUR)|
# |---------------|----------|---------------------------|-------|--------------------------- |
# | Banana        |   2      |                     800.00| 25    | 2000.00                    |
# ===========================================================================================

ime_proizvoda = input("Ime proizvoda: ")
kolicina = float(input("Broj komada: "))
cijena_1_kom_bez_pdv = float(input("Cijena 1 kom bez PDV (EUR): "))
pdv_posto = float(input("PDV (%): "))

cijena_1_kom_s_pdv = cijena_1_kom_bez_pdv * (1 + pdv_posto / 100)
ukupna_cijena_pdv = kolicina * cijena_1_kom_s_pdv

naziv_kategorije_ime_proizvoda = " Ime proizvoda "
naziv_kategorije_kolicina = " Količina "
naziv_kategorije_cijena_1_kom_bez_pdv = " Cijena 1 kom bez PDV (EUR) "
naziv_kategorije_pdv = " PDV (%) "
naziv_kategorije_ukupna_cijena = " Ukupna cijena s PDV (EUR) "
broj_kategorija = 5
broj_vertikalni_rubova = broj_kategorija + 1


duljina_naziv_kategorije_ime_proizvoda = max(
    len(naziv_kategorije_ime_proizvoda), len(ime_proizvoda)
)
duljina_naziv_kategorije_kolicina = len(naziv_kategorije_kolicina)
duljina_naziv_kategorije_cijena_1_kom_bez_pdv = len(
    naziv_kategorije_cijena_1_kom_bez_pdv
)
duljina_naziv_kategorije_pdv = len(naziv_kategorije_pdv)
duljina_naziv_kategorije_ukupna_cijena = len(naziv_kategorije_ukupna_cijena)

broj_vertikalni_odjeljaka_za_rubove = 2

maksimalana_duljina_retka = (
    duljina_naziv_kategorije_ime_proizvoda
    + duljina_naziv_kategorije_kolicina
    + duljina_naziv_kategorije_cijena_1_kom_bez_pdv
    + duljina_naziv_kategorije_pdv
    + duljina_naziv_kategorije_ukupna_cijena
    + broj_vertikalni_rubova
) - broj_vertikalni_odjeljaka_za_rubove

ograda_pocetak_kraj = "=" * maksimalana_duljina_retka
ograda_sredina = "-" * maksimalana_duljina_retka

formatiranje_cijene = f">{duljina_naziv_kategorije_cijena_1_kom_bez_pdv},.2f"

print(f"|{ograda_pocetak_kraj}|")
print(
    f"|{naziv_kategorije_ime_proizvoda:^{duljina_naziv_kategorije_ime_proizvoda}}|{naziv_kategorije_kolicina}|{naziv_kategorije_cijena_1_kom_bez_pdv}|{naziv_kategorije_pdv}|{naziv_kategorije_ukupna_cijena}|"
)
print(f"|{ograda_sredina}|")

print(
    f"|{ime_proizvoda:^{duljina_naziv_kategorije_ime_proizvoda}}|{kolicina:^{duljina_naziv_kategorije_kolicina}.1f}|{cijena_1_kom_bez_pdv:{formatiranje_cijene}}|{pdv_posto:>{duljina_naziv_kategorije_pdv}.0}|{ukupna_cijena_pdv:{formatiranje_cijene}}|"
)

print(f"|{ograda_pocetak_kraj}|")
