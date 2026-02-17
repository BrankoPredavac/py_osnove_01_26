ime_i_prezime: str = "Marko Maric"
ocjena_na_zavrsnom_ispitu: int = 4
diplomirao: bool = ocjena_na_zavrsnom_ispitu > 1
# "Ime: ""Marko Maric"
# "Ime: Marko Maric"

# ispis_ime = "Ime: " + ime_i_prezime
# ispis_ocjena_na_zavrsnom_ispitu = "Ocjena na zavrsnom ispitu: " + str(
#     ocjena_na_zavrsnom_ispitu
# )
# ispsi_diplomirao = "Diplomirao: " + str(diplomirao)

# f"Ime: {ime_i_prezime}"
# "Ime: Marko Maric"
ispis_ime = f"Ime: {ime_i_prezime}"
ispis_ime_svasta = (
    f"{ime_i_prezime} Ime: {ime_i_prezime} {ime_i_prezime} {ime_i_prezime}"
)

ispis_ocjena_na_zavrsnom_ispitu = (
    f"Ocjena na zavrsnom ispitu: {ocjena_na_zavrsnom_ispitu}"
)

ispsi_diplomirao = f"Diplomirao: {diplomirao}"

print(ispis_ime)
print(ispis_ocjena_na_zavrsnom_ispitu)
print(ispsi_diplomirao)
