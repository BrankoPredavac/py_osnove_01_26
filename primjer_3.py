cijena_bez_pdv_eur = 200

print(id(cijena_bez_pdv_eur))

pdv = 0.25
print(id(pdv))

cijena_s_pdv_eur = cijena_bez_pdv_eur + cijena_bez_pdv_eur * pdv
print(cijena_s_pdv_eur)
print(id(cijena_s_pdv_eur))
