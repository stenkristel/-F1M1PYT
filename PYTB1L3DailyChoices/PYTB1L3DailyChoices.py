print("De princess bedankt je voor het doden van de draak. Ze zegt: 'Ik ben je voor e.....'")
print("En op dat moment gaat je wekker, blijf je nog even liggen of ga je eruit zodat je rustig aan kan doen")
print("typ: VERDERSLAPEN of OPSTAAN")

choice = input()
if choice == 'VERDERSLAPEN':
    print("Je valt gelijk in slaap en het voelt geen seconde later en je wekker gaat weer, je moet er nu echt uit.")
elif choice == 'OPSTAAN':
    print("Je staat op en je heb gelijk spijt, maar je hebt geen zin om te haasten 'zucht...'")
else:
    print("foute keuze")

print("Je doet je kast open en je hebt alleen nog een spijkerbroek, een trui en een T-shirt, wat doe je aan?")
print("typ: 'T-SHIRT' of 'TRUI'")

choice = input()
if choice == 'T-SHIRT':
    print("Je doet een T-shirt aan en het voelt nu al koud.")
elif choice == 'TRUI':
    print("Je doet een trui aan en het voelt nu al warm.")
else:
    print("foute keuze")

print("Je hebt honger, het enige in huis is chocolade hagel, wat droog brood en volkoren beschuit, wat ga je eten?")
print("typ: BROOD of BESCHUIT")

choice = input()
if choice == 'BROOD':
    print("Je eet het brood op en je maag begint te knorren, dat was iets te oud brood...")
elif choice == 'BESCHUIT':
    print("Je eet het beschuit en je maag begint te knorren, dat was niet genoeg eten, maar je hebt geen tijd meer.")
else:
    print("foute keuze")

print("Je gaat nu je tas inpakken. Neem je een lekkere snack mee of een stuk fruit?")
print ("SNACK of FRUIT")

choice = input()
if choice == 'SNACK':
    print("Je doet een chocolade reep in je tas")
elif choice == 'FRUIT':
    print("Je doet een appel in je tas")
else:
    print("foute keuze")

print("Je stapt de deur uit, ga je met de fiets of ga je met de bus?")
print("type: BUS of FIETS")

choice = input()
if choice == 'BUS':
    print("Je stapt de bus in en het ruikt naar zweet, was je maar met de fiets gegaan...")
elif choice == 'FIETS':
    print("Je stapt op de fiets en na twintig trappen ben je al moe, was je maar met de bus gegaan...")
else:
    print("foute keuze")