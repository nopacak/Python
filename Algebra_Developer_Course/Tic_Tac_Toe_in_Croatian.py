# IGRA KRIZIC-KRUZIC

# igrač 1 -> X
# igrač 2 -> O
# (pobjeda jednog igrača ili neriješeno)

# Sve dok igra nije gotova:
#   iscrtati ploču:
#       brojevi polja, odabrana polja igrača, ekran se svaki puta mora očistiti -> "python how to clear console"
#   definirati koji igrač trenutno igra:
#       pitati igrača da odabere neko polje
#   validacija je li ispravno odabrano
#   provjera stanja igre (pobjeda?, neriješeno?, još uvijek možemo igrati?)
#   ovisno o statusu nastaviti igru ili zaustaviti

import os

# DEFINIRANJE VARIJABLI
polja_na_ploci = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
igraj_igru = True
gotova_igra = False
red = 0
prethodni_red = -1

# DEFINIRANJE FUNKCIJA
def iscrtaj_plocu(polja_na_ploci: dict) -> str:
    """Funkcija za iscrtavanje ploče za križić-kružić igru

    Args:
        polja_na_ploci (dict): Vrijednosti unutar polja su dodijeljene ključevima

    Returns:
        str: Ispis ploče
    """
    ploca = (f"\n {polja_na_ploci[1]} | {polja_na_ploci[2]} | {polja_na_ploci[3]} \n-----------\n"
             f" {polja_na_ploci[4]} | {polja_na_ploci[5]} | {polja_na_ploci[6]} \n-----------\n"
             f" {polja_na_ploci[7]} | {polja_na_ploci[8]} | {polja_na_ploci[9]}\n")
    print(ploca)


def provjeri_redoslijed_igraca(red: int) -> str:
    """Funkcija za provjeru redoslijeda igrača

    Args:
        red (int): Računa se modulus

    Returns:
        str: Vraća se znak za igrača ("X" ili "O")
    """
    if red % 2 == 0:
        return "O"
    else:
        return "X"


def provjeri_stanje_igre(polja_na_ploci: dict) -> bool:
    """Funkcija za provjeru uvjeta za završetak igre

    Args:
        polja_na_ploci (dict): Popis kombinacija polja koji zadovoljavaju uvjete za završetak igre

    Returns:
        bool: Ako su uvjeti za završetak igre zadovoljeni, vraća se true 
    """
    # Provjera horizontalnih linija
    if (polja_na_ploci[1] == polja_na_ploci[2] == polja_na_ploci[3]) \
    or (polja_na_ploci[4] == polja_na_ploci[5] == polja_na_ploci[6]) \
    or (polja_na_ploci[7] == polja_na_ploci[8] == polja_na_ploci[9]):
        return True
    # Provjera vertikalnih linija
    elif (polja_na_ploci[1] == polja_na_ploci[4] == polja_na_ploci[7]) \
    or (polja_na_ploci[2] == polja_na_ploci[5] == polja_na_ploci[8]) \
    or (polja_na_ploci[3] == polja_na_ploci[6] == polja_na_ploci[9]):
        return True
    # Provjera dijagonalnih linija
    elif (polja_na_ploci[1] == polja_na_ploci[5] == polja_na_ploci[9]) \
    or (polja_na_ploci[3] == polja_na_ploci[5] == polja_na_ploci[7]):
        return True
    else:
        return False


# KOD ZA POKRETANJE IGRE
while igraj_igru:
    os.system('cls' if os.name == 'nt' else 'clear')
    iscrtaj_plocu(polja_na_ploci)
    if prethodni_red == red:
        print("Neispravan unos, odaberite drugo polje molim!")
    prethodni_red = red
    odabir_igrača = input("Igrač " + str((red % 2) + 1) + "\nUnesite broj polja na koje želite staviti svoj znak: ")
    # Provjeri da li je igrač upisao brojeve od 1 do 9
    if str.isdigit(odabir_igrača) and int(odabir_igrača) in polja_na_ploci:
        # Provjeri da li je odabrano polje već zauzeto
        if not polja_na_ploci[int(odabir_igrača)] in {"X", "O"}:
            red += 1
            polja_na_ploci[int(odabir_igrača)] = provjeri_redoslijed_igraca(red)
    # Provjeri stanje igre
    if provjeri_stanje_igre(polja_na_ploci):
        igraj_igru, gotova_igra = False, True
    if red > 8:
        igraj_igru = False



# PRINTANJE REZULTATA
os.system('cls' if os.name == 'nt' else 'clear')
iscrtaj_plocu(polja_na_ploci)
# Ako ima pobjednika
if gotova_igra:
    if provjeri_redoslijed_igraca(red) == "X":
        print("Igrač 1 je pobijedio!")
    else:
        print("Igrač 2 je pobijedio!")
# Ako je neriješeno
else:
    print("Neriješen rezultat!")
    
