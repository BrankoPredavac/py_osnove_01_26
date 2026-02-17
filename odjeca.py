robot_vadi_iz_susilice = "carapa"

# da robot moze izvadiitr vise stvari odjednom iz susilice
# Bez obzir akojeg je tipa ja cu minimalno ispitiati uvijek 4 tipa
if robot_vadi_iz_susilice == "majica":
    print("Slaze majicu na policu s majicama")

if robot_vadi_iz_susilice == "hlace":
    print("Slaze hlace na policu s hlace")

if robot_vadi_iz_susilice == "carapa":
    print("Slaze carapu u ladicu s carapama")

if robot_vadi_iz_susilice == "haljina":
    print("Vjesa haljinu na vjesalicu")


# da robot moze izvaditi SAMO JEDAN odjevni predmet iz susilice
# najgori slucaj 4 uvjet aispitujem, kad nadim istinit druge ne gledam dalje
# Najcesci odjevni predmeti od najcesceg prema najrjedem: majici, hlace, carape, haljine
if robot_vadi_iz_susilice == "majica":
    print("Slaze majicu na policu s majicama")

elif robot_vadi_iz_susilice == "hlace":
    print("Slaze hlace na policu s hlace")

elif robot_vadi_iz_susilice == "carapa":
    print("Slaze carapu u ladicu s carapama")

elif robot_vadi_iz_susilice == "haljina":
    print("Vjesa haljinu na vjesalicu")


if robot_vadi_iz_susilice == "carapa":
    print("Slaze carapu u ladicu s carapama")

elif robot_vadi_iz_susilice == "majica":
    print("Slaze majicu na policu s majicama")

elif robot_vadi_iz_susilice == "hlace":
    print("Slaze hlace na policu s hlace")

elif robot_vadi_iz_susilice == "haljina":
    print("Vjesa haljinu na vjesalicu")

print("Gotovo")
