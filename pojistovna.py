from pojisteny import Pojisteny

pojisteny = Pojisteny

seznam_pojistenych = []
seznam_pojistenych.append(Pojisteny("Jan", "Novák", 30, 111111111))
seznam_pojistenych.append(Pojisteny("Josef", "Nový", 25, 111111112))
seznam_pojistenych.append(Pojisteny("Jana", "Nová", 31, 111111113))
seznam_pojistenych.append(Pojisteny("Josefina", "Nováková", 24, 111111114))

while True:
    print()
    print("-------------------------------------")
    print("Evidence pojištěných.")
    print("-------------------------------------")
    print()
    print("Vyberte požadovanou akci")
    print()
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného")
    print("4 - Vyhledat pojištěného pomocí počátečních písmen jména")
    print("5 - Vyhledat pojištěného pomocí počátečních písmen příjmení")
    print("6 - Konec")
    print()

    while True:
        try:
            moznost = int(input("Vaše volba 1-6: "))
            break
        except:
            print("Nezadali jste číslo!")

    if moznost == 1:
        print("Zadejte údaje nového pojištěného ")
        nove_jmeno = input("Zadejte jméno pojištěného: ")
        nove_prijmeni = input("Zadejte příjmení: ")
        novy_telefon = input("Zadejte telefonní číslo: ")
        novy_vek = input("Zadejte věk: ")
        print("Data byla uložena.")
        seznam_pojistenych.append(Pojisteny(nove_jmeno, nove_prijmeni, novy_telefon, novy_vek))

    elif moznost == 2:
        print("Všichni pojištění")
        for pojisteny in seznam_pojistenych:
            print(pojisteny)

    elif moznost == 3:
        print("Vyhledat pojisteneho")
        hledane_jmeno = input("Zadej hledané jméno: ").capitalize()
        hledane_prijmeni = input("Zadej hledané příjmení: ").capitalize()
        for pojisteny in seznam_pojistenych:
            pojisteny.vyhledat_pojisteneho(hledane_jmeno, hledane_prijmeni)

    elif moznost == 4:
        print("Vyhledat pomocí počátečních písmen jména")
        zacatek_jmena = input("Zadejte počíteční písmeno, nebo písmena křestního jména: ").capitalize()
        for pojisteny in seznam_pojistenych:
            pojisteny.vyhledat_zacatek_jmena(zacatek_jmena)

    elif moznost == 5:
        print("Vyhledat pomocí počátečních písmen příjmení ")
        zacatek_prijmeni = input("Zadejte počíteční písmeno, nebo písmena příjmení:" ).capitalize()
        for pojisteny in seznam_pojistenych:
            pojisteny.vyhledat_zacatek_prijmeni(zacatek_prijmeni)

    elif moznost == 6:
        print("Konec")
        break

    else:
        print("Zadali jste špatnou možnost")