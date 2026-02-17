okus_sladoleda = (
    input(
        "Koji okus sladoleda zelis (odaberi broj):\n\t1. Vanilija\n\t2. Cokolada\n\t3. Pistacio\n>"
    )
    .strip()
    .lower()
)

if okus_sladoleda == "1":
    print("Stavljam kuglicu cokolade")

    zeli_li_slag = input("Zelis li slag na sladoledu? (Y/N)> ").strip().lower()
    if zeli_li_slag == "y":
        print("Stavljam slag na sladoled")

    zeli_li_coko_mrvice = (
        input("Zelis li cokoladne mrvice na sladoledu? (Y/N)> ").strip().lower()
    )
    if zeli_li_coko_mrvice == "y":
        print("Stavljam cokoladne mrvice na sladoled")

    zeli_li_keks = (
        input("Zelis li komadice keksa na sladoledu? (Y/N)> ").strip().lower()
    )
    if zeli_li_keks == "y":
        print("Stavljam koamdice keksa na sladoled")

elif okus_sladoleda == "2":
    print("Stavljam kuglicu vanilije")

    zeli_li_slag = input("Zelis li slag na sladoledu? (Y/N)> ").strip().lower()
    if zeli_li_slag == "y":
        print("Stavljam slag na sladoled")

    zeli_li_coko_mrvice = (
        input("Zelis li cokoladne mrvice na sladoledu? (Y/N)> ").strip().lower()
    )
    if zeli_li_coko_mrvice == "y":
        print("Stavljam cokoladne mrvice na sladoled")

    zeli_li_keks = (
        input("Zelis li komadice keksa na sladoledu? (Y/N)> ").strip().lower()
    )
    if zeli_li_keks == "y":
        print("Stavljam koamdice keksa na sladoled")

elif okus_sladoleda == "3":
    print("Stavljam kuglicu pistacio")

    zeli_li_slag = input("Zelis li slag na sladoledu? (Y/N)> ").strip().lower()
    if zeli_li_slag == "y":
        print("Stavljam slag na sladoled")

    zeli_li_coko_mrvice = (
        input("Zelis li cokoladne mrvice na sladoledu? (Y/N)> ").strip().lower()
    )
    if zeli_li_coko_mrvice == "y":
        print("Stavljam cokoladne mrvice na sladoled")

    zeli_li_keks = (
        input("Zelis li komadice keksa na sladoledu? (Y/N)> ").strip().lower()
    )
    if zeli_li_keks == "y":
        print("Stavljam koamdice keksa na sladoled")
