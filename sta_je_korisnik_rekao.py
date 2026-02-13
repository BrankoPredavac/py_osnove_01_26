# Pitati korsniak da odogovri Yes or No
# Korisnik odogovorio Yes: <Njegov odogovor>
# Korisnik odogovorio No: <Njegov odogovor>

# YES, Yes, yes, y, Y
# No, NO, N, n

odgovor_korisnika = input("Drago korsncie jesu li podatci ispravni (Y/N)> ")

je_li_yes = (
    (odgovor_korisnika == "YES")
    or (odgovor_korisnika == "yes")
    or (odgovor_korisnika == "yeS")
    or (odgovor_korisnika == "yEs")
    or (odgovor_korisnika == "Yes")
    or (odgovor_korisnika == "yES")
    or (odgovor_korisnika == "YEs")
    or (odgovor_korisnika == "y")
    or (odgovor_korisnika == "Y")
)

print("Korisnik odogovorio Yes:", je_li_yes)

mala_slova_odgoovr_korisnika = odgovor_korisnika.lower()
je_li_yes = (mala_slova_odgoovr_korisnika == "yes") or (
    mala_slova_odgoovr_korisnika == "y"
)

print("Korisnik odogovorio Yes:", je_li_yes)

je_li_no = (
    (odgovor_korisnika == "NO")
    or (odgovor_korisnika == "no")
    or (odgovor_korisnika == "n")
    or (odgovor_korisnika == "N")
    or (odgovor_korisnika == "No")
    or (odgovor_korisnika == "nO")
)

print("Korisnik odogovorio No:", je_li_no)

mala_slova_odgoovr_korisnika = odgovor_korisnika.upper()
je_li_no = (mala_slova_odgoovr_korisnika == "NO") or (
    mala_slova_odgoovr_korisnika == "N"
)

print("Korisnik odogovorio No:", je_li_no)
