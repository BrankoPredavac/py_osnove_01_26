# napravite varijablu godine
# i usporedite da li je osoba maloljetna, mladoj zivotnoj dobi, zlatni godine, pred mirovinu umrovljenik
# maloljetan, mladi od 18
# mladoj zivotnoj dobi, od 18 do 30
# zlatne godine od 30 do 50
# pred mirovinu od 50 do 65
# u mirovini od 65
# svaki rezulktat pohranite u novu varijablu

godine = 80

maloljetan = godine < 18
mlada_zivotna_dob = (godine >= 18) and (godine < 30)
# mlada_zivotna_dob = (godine < 30) and (godine >= 18)
zlatne_godine = (godine >= 30) and (godine < 50)
pred_mirovinu = (godine >= 50) and (godine < 65)
u_mirovini = godine >= 65

print(maloljetan)
print(mlada_zivotna_dob)
print(zlatne_godine)
print(pred_mirovinu)
print(u_mirovini)


maloljetan = godine < 18
u_mirovini = godine >= 65
mlada_zivotna_dob = (not maloljetan) and (godine < 30)
# mlada_zivotna_dob = (godine < 30) and (godine >= 18)
zlatne_godine = (not maloljetan) and (not mlada_zivotna_dob) and (godine < 50)
pred_mirovinu = (
    (not maloljetan)
    and (not mlada_zivotna_dob)
    and (not zlatne_godine)
    and (godine < 65)
)

pred_mirovinu = (not u_mirovini) and (godine >= 50)

print()
print(maloljetan)
print(mlada_zivotna_dob)
print(zlatne_godine)
print(pred_mirovinu)
print(u_mirovini)
