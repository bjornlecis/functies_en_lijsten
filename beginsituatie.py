""""
In dit programma passen we diverse functies toe op een lijst.
De gebruiker geeft een invoer welke functie hij wil aanroepen
indien de gebruiker stop invoert stop het programma
"""
#deze functie drukt de mogelijkheden af
def print_mogelijke_functies():
    print("je kan kiezen uit")
    print("1: Toon lijst om de lijst te tonen")
    print("2: voeg toe om een naam toe te voegen")
#deze functie geeft de lijst van de namen
def print_lijst(lijst):
    print("de namen in de lijst zijn")
    for element in lijst:
        print(element)

#lijst met namen(hardcoded)
namen = ["Bart","Sofie","Mark","Evelien"]


#hoofdprogramma
print_mogelijke_functies()
invoer = input("Wat wil je doen? geed het nummer in of stop om te stoppen")
while(not invoer == "stop"):
    if(invoer == "1"):
        print_lijst(namen)



    print_mogelijke_functies()
    invoer = input("Wat wil je doen? geed het nummer in of stop om te stoppen")


