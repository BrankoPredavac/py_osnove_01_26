pocetni_string = "27"

print(f"{pocetni_string}   {type(pocetni_string)}")


pocetni_int = int(pocetni_string)
print(f"{pocetni_int}   {type(pocetni_int)}")

pocetni_float = float(pocetni_string)
print(f"{pocetni_float}   {type(pocetni_float)}")


pocetni_bool = bool(pocetni_string)
print(f"{pocetni_bool}   {type(pocetni_bool)}")


prazni_int = int()
prazni_string = str()
prazni_float = float()
prazni_bool = bool()
prazna_lista = list()

print("False", type("False"), bool("False"))
print("0", type("0"), bool("0"))
print("0.0", type("0.0"), bool("0.0"))
print("false", type("false"), bool("false"))

print("Gotovo")
