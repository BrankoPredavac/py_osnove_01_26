# kalkulator + - / * ^ % //
# prvi broj
# drugi broj
# operaciju
# operacija ne psotoji ako korisnik odabere krivo

# prvi broj + drugi broj = rezultat
print("================ KALKULATOR =================")
print(" Operacije: + - / * ^ % //", end="\n\n")

prvi_broj = float(input("Dragi korisncie, daj mi prvi broj> "))
drugi_broj = float(input("Dragi korisncie, daj mi drugi broj> "))
operacija = input("Izaberi jednu operaciju (+ - / * ^ % //)> ").strip()

validna_operacija = (
    (operacija == "+")
    or (operacija == "-")
    or (operacija == "*")
    or (operacija == "/")
    or (operacija == "%")
    or (operacija == "^")
    or (operacija == "//")
) and not ((operacija == "/") and drugi_broj == 0)

# validna_operacija = operacija in ("+", "-", "*", "/", "%", "^", "//")

if operacija == "+":
    rezultat = prvi_broj + drugi_broj

elif operacija == "-":
    rezultat = prvi_broj - drugi_broj

elif operacija == "*":
    rezultat = prvi_broj * drugi_broj

elif operacija == "/":
    if drugi_broj != 0:
        rezultat = prvi_broj / drugi_broj

elif operacija == "^":
    rezultat = prvi_broj**drugi_broj

elif operacija == "%":
    rezultat = prvi_broj % drugi_broj

elif operacija == "//":
    rezultat = prvi_broj // drugi_broj


if validna_operacija:
    print(f"{prvi_broj} {operacija} {drugi_broj} = {rezultat}")
else:
    print("Odabrao si operaciju koja nije podrzana")
