class Osoba:
    def __init__(self, ime, prezime, email, telefon, adresa):
        self.ime = ime
        self.prezime = prezime
        self.email = email
        self.telefon = telefon
        self.adresa = adresa

    def __str__(self) -> str:
        return f"Osoba({self.ime}, {self.prezime}, {self.email}, {self.telefon}, {self.adresa})"
    

class Djelatnik(Osoba):
    def __init__(self, ime, prezime, email, telefon, adresa, radno_mjesto):
        super().__init__(ime, prezime, email, telefon, adresa)
        self.radno_mjesto = radno_mjesto

    def __str__(self) -> str:
        return f"Djelatnik({self.ime}, {self.prezime}, {self.email}, {self.telefon}, {self.adresa}, {self.radno_mjesto})"


class Kupac(Osoba):
    def __init__(self, ime, prezime, email, telefon, adresa, oib):
        super().__init__(ime, prezime, email, telefon, adresa)
        self.oib = oib

    def __str__(self) -> str:
        return f"Kupac(ime={self.ime}, prezime={self.prezime}, email={self.email}, telefon={self.telefon}, adresa={self.adresa}, oib={self.oib})"


djelatnici = []
while True:
    ime = input("Unesite ime: ")
    prezime = input("Unesite prezime: ")
    email = input("Unesite email: ")
    telefon = input("Unesite telefon: ")
    adresa = input("Unesite adresa: ")
    radno_mjesto = input("Unesite radno mjesto: ")
    
    djelatnik = Djelatnik(ime, prezime, email, telefon, adresa, radno_mjesto)
    djelatnici.append(djelatnik)

    if input("Želite li dodati još jednog djelatnika? (d/n) ") != "d":
        break


kupci = []
while True:
    ime = input("Unesite ime: ")
    prezime = input("Unesite prezime: ")
    email = input("Unesite email: ")
    telefon = input("Unesite telefon: ")
    adresa = input("Unesite adresa: ")
    oib = input("Unesite OIB: ")
    
    kupac = Kupac(ime, prezime, email, telefon, adresa, oib)
    kupci.append(kupac)

    if input("Želite li dodati još jednog kupca? (d/n) ") != "d":
        break


for djelatnik in djelatnici:
    print(djelatnik)

print()

for kupac in kupci:
    print(kupac)


# Djelatnik(Ana, Anic, ana@ana, 123, Adresa 1, 1)
# Djelatnik(Pero, Peric, pero@pero, 321, Adresa 2, mjesto 2)

# Kupac(Marko, Markic, marko@marko, 789, Adresa 3, 12345678)

kupac = Kupac(ime="Marko", prezime="Markic", email="marko@marko", telefon=789, adresa="Adresa 3", oib="12345678")
print(kupac)
# Kupac(Marko, Markic, marko@marko, 789, Adresa 3, 12345678)
# Kupac(ime=Marko, prezime=Markic, email=marko@marko, telefon=789, adresa=Adresa 3, oib=12345678)