import random
import time
import os
from listy_slow import slowa, rzeczowniki, przymiotniki

def clear():
    os.system( 'cls' )
#PROJEKT GRY WISIELEC

wstep = """
Zagrajmy w WISIELCA! :)
---------
|       |
|       O
|      /|\\
|      / \\
|
|

ZASADY:
1. Masz 20 prób, aby zgadnąć słowo. Słowo jest wybierane automatycznie przez grę. 
2. Po 7 nieudanych próbach przegrywasz.
3. Podajesz po jednej literze (nieważne, czy dużej czy małej), ale bez polskich znaków!
4. Po każdej próbie wyświetla się aktualny stan wisielca oraz ilość twoich prób, trafionych i nietrafionych liter.
"""


print(wstep)
time.sleep(6)
zgadl = False
proby = 20
trafione = list()
nietrafione = list()

wisielce = [ 
"""
			---------
			| 
			|
			|
			|
			|
			|
			|
			-
		""",
		"""
			---------
			|       |
			|
			|
			|
			|
			|
			|
			-
		""",
		"""
			---------
			|       |
			|       O
			|
			|
			|
			|
			|
			-
		""",
		"""
			---------
			|       |
			|       O
			|       |
			|
			|
			|
			|
			-
		""",
		"""
			---------
			|       |
			|       O
			|       |
			|      /
			|
			|
			|
			-
		""",
		"""
			---------
			|       |
			|       O
			|       |
			|      / \\
			|
			|
			|
			-
		""",
		"""
			---------
			|       |
			|       O
			|       |\\
			|      / \\
			|
			|
			|
			-
		""",
		"""
			---------
			|       |
			|       O
			|      /|\\
			|      / \\
			|
			|
			|
			-
		"""
]

stan = 0
slowo = random.choice(slowa)
if slowo in rzeczowniki:
	print(f"Haslo jest rzeczownikiem i zawiera {len(slowo)} liter")
else:
	print(f"Haslo jest przymiotnikiem i zawiera {len(slowo)} liter")
slowo = slowo.upper()
print("\n")

zaczynamy = input("Jesli jestes gotowy/a wcisnij ENTER!")
clear()

niewiadome = "_ " * len(slowo)
print(wisielce[stan])
print(f'Słowo: {niewiadome}  |  Pozostale proby = {proby}  |  Trafione: 0  |  Nietrafione: 0')
print("\n")


while proby > 0 and stan != 7 and not zgadl:

	traf = input("Podaj jedną literę:")
	traf = traf.upper()
	clear()

	if traf in trafione or traf in nietrafione:
		print("Ta litera byla juz wybrana!")
	else:
		if traf in slowo:
			print(f"Tak! Litera {traf} znajduje się w haśle!")
			trafione.append(traf)
			lista_niewiadome_bez_spacji = list(niewiadome.replace(" ", ""))
			indeksy = [i for i, x in enumerate(slowo) if x == traf]
			for indeks in indeksy:
				lista_niewiadome_bez_spacji[indeks] = traf
			niewiadome = " ".join(lista_niewiadome_bez_spacji)
			proby = proby - 1
			print(f'{wisielce[stan]}')
			print(f'Słowo: {niewiadome}  |  Pozostale proby = {proby}  |  Trafione: {trafione}  |  Nietrafione: {nietrafione}')
			if '_' not in niewiadome:
				zgadl = True
				print("GRATULACJE!")
			print("\n")
		if traf not in slowo:
			print(f'Nie! Litera {traf} nie znajduje sie w haśle!')
			nietrafione.append(traf)
			stan = stan + 1
			proby = proby - 1
			print(f'{wisielce[stan]}')
			print(f'Słowo: {niewiadome}  |  Pozostale proby = {proby}  |  Trafione: {trafione}  |  Nietrafione: {nietrafione}')
			if stan == 7:
				print("GAME OVER!")
			if proby == 0:
				print("SKONCZYLA CI SIE MOZLIWA LICZBA PROB!")
				print("GAME OVER!")
			print("\n")

print(f'Haslo: {slowo}')
print("\n")
Koniec = input("Nacisnij ENTER żeby zamknąć grę.")



