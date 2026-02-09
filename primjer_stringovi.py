moj_string = "Ovo je tekst"
moj_string = "Ovo je tekst"
# moj_tekst = "On je rekao: "Idemo uciti python""
# moj_tekst = (On je rekao: )Idemo uciti python()
# moj_tekst = 'On je rekao: 'Idemo uciti python''
moj_string = """
Moj tekste
Ide ovdje

"""

print(moj_string)


moj_string = """
Moj tekste
Ide ovdje


"""

print(moj_string)

print(bool("None"))
print(bool("0"))
print(bool("False"))
print(bool(""))

print(len(moj_string))

moj_string_2 = "ovo je tekst"

print(len(moj_string_2))

print()
print(moj_string_2)
print(moj_string_2.capitalize())
print(moj_string_2.upper())
print(moj_string_2.lower())

moj_string_2 = "22"
MOJ_STRING_2 = "22"

tekst_1 = "DA"
tekst_2 = "da"

print(tekst_1 != tekst_2)
print("DA" != "da")

print(id(moj_string_2) == id(MOJ_STRING_2))

moj_tekst_3 = "Idemo " + " dalje " + " -----> "
print(moj_tekst_3)
moj_tekst_3 = "Idemo  dalje  -----> "
print(moj_tekst_3)

moj_tekst_4 = "Idemo " * 5
print(moj_tekst_4)
