# primjer = "Ante ide doma. Igrat ce se na PC-u."
# print(primjer.count("."))

# Unesi rečenicu od korisnika:
# izbrojite koliko ima samoglasnika
# prosjek samoglsanika u toj recenici: broj samoglsnika/ brojem znakova u recenici

recenica = input(
    "Dragi korisnice daj mi neku recenicu za koju zelis da ti izbrojim broj samoglsnika i prosjek> "
)

recenica_malim_slovima = recenica.lower()

broj_samoglasnika_a = recenica_malim_slovima.count("a")
broj_samoglasnika_e = recenica_malim_slovima.count("e")
broj_samoglasnika_i = recenica_malim_slovima.count("i")
broj_samoglasnika_o = recenica_malim_slovima.count("o")
broj_samoglasnika_u = recenica_malim_slovima.count("u")

zbroj_samoglasnika = (
    broj_samoglasnika_a
    + broj_samoglasnika_e
    + broj_samoglasnika_i
    + broj_samoglasnika_o
    + broj_samoglasnika_u
)


print("U recenici")
print(recenica)
print("Broj samoglasnika:", zbroj_samoglasnika)

prosjek_samglasnika_u_recenici = zbroj_samoglasnika / len(recenica)

print("prosjek samoglasnika u recenici:", prosjek_samglasnika_u_recenici, "znakova")
