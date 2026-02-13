# Unesi ime, prezime i grad:
# kako god korisnik unio ulaz popravite taj tekst pravopisno
# Pocetno veliko slovo za ime i prezime i grad
# Dobrodošao <ime> <prezime> iz <ime grada>

ime = input("Dragi korsinice, daj mi svoje ime> ")
prezime = input("Dragi korsinice, daj mi svoje prezime> ")
ime_grad = input("Dragi korsinice, daj mi naziv grada u kojem se nalazis> ")

ispis = "Dobrodošao " + ime.title() + " " + prezime.title() + " iz " + ime_grad.title()
print(ispis)

print("Dobrodošao", ime.title(), prezime.title(), "iz", ime_grad.title())
