
import random

while True:
    dobas = input("Dobókocka Dobas(Enter): \n")
    # dobókocka számai és randomizálása
    szamok = ["1", '2', '3', '4', '5', '6']
    dobas_eredmenye = random.choice(szamok)
    print(f"a Dobókocka eredménye: {dobas_eredmenye} \n")
