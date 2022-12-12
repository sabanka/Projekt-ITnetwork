
class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return(f"{self.jmeno} {self.prijmeni} {self.vek} {self.telefon}")

    def vypis(self):
        print(f"{self.jmeno}, {self.prijmeni}, {self.vek}, {self.telefon}")

    def vyhledat_pojisteneho(self, hledane_jmeno, hledane_prijmeni):
        if hledane_jmeno == self.jmeno and hledane_prijmeni == self.prijmeni:
            self.vypis()

    def vyhledat_zacatek_jmena(self, zacatek_jmena):
        if self.jmeno.startswith(zacatek_jmena):
            self.vypis()

    def vyhledat_zacatek_prijmeni(self, zacatek_prijmeni):
        if self.prijmeni.startswith(zacatek_prijmeni):
            self.vypis()