# Pitati korisnika za visinu (u cm) i težinu (u kg)
# BMI = težina / (visina_m * visina_m)
# - manji od 18.5: "Mršav – jedi više proteina!"
# - 18.5-24.9: "Idealna kondicija – super!"
# - 25-29.9: "Vanjski – više kardio vježbi."
# - veci od 30: "Pretio – vrijeme za promjene!"

# Visina: 175 cm
# Težinu: 70 kg
# Tvoj BMI je: 22.9
# Idealna kondicija – super!
print("Dobro dosli u program za racunanje indeksa tjelsne mase :-)", end="\n\n")

visina_cm = int(input(r"Dragi krosinice koliko si visok\a (cm)> "))
masa_kg = float(input(r"Dragi krosinice kolika ti je masa (kg)> "))

visina_m = visina_cm / 100
bmi_indeks = masa_kg / (visina_m**2)

bmi_poruka = ""

if bmi_indeks < 18.5:
    bmi_poruka = "Mršav – jedi više proteina!"
elif bmi_indeks < 25:
    bmi_poruka = "Idealna kondicija – super!"
elif bmi_indeks < 30:
    bmi_poruka = "Vanjski – više kardio vježbi."
else:
    bmi_poruka = "Pretio – vrijeme za promjene!"

print(f"Visina: {visina_cm} cm")
print(f"Tezina: {masa_kg:.2f} kg")
print(f"Tvoj BMI je: {bmi_indeks:.2f}")
print(bmi_poruka)
