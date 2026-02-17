stranica_a_trokuta_cm = 5
stranica_b_trokuta_cm = 7
stranica_c_trokuta_cm = 11

# Povrsina toruka, prikazi na ekranu rezultat
povrsina_tokuta_cm2 = (stranica_a_trokuta_cm * stranica_b_trokuta_cm) / 2

# print("Povrsina trokuta", povrsina_tokuta_cm2, "cm^2")

print(f"Povrsina trokuta {povrsina_tokuta_cm2} cm^2")

# Opseg trokuta, prikazi na ekranu rezultat
opseg_trokuta_cm = stranica_a_trokuta_cm + (
    stranica_b_trokuta_cm + stranica_c_trokuta_cm
)
# print("Opseg trokuta", opseg_trokuta_cm, "cm")

print(f"Opseg trokuta {opseg_trokuta_cm} cm")
