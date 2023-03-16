import time

def horloge():
    heures = int(input('quelles heures est-il : '))
    minutes = int(input("combien de minute y'a t-il : "))
    secondes = int(input('combien de secondes avons nous : '))
    alarmes_heures = int(input("l'heure de l'alarme : "))
    alarmes_minutes = int(input("les minutes de l'alarme : "))
    alarmes_secondes = int(input("les secondes de l'alarme : "))
    while heures < 24:
            while minutes < 60:
                    while secondes < 60:
                        if heures == alarmes_heures:
                            if minutes == alarmes_minutes:
                                if secondes == alarmes_secondes:
                                    print("bip bip bip")
                        print(heures,':',minutes,':',secondes)
                        time.sleep(1)
                        secondes=secondes+1
                    secondes=0
                    minutes=minutes+1
            heures=heures+1
            minutes=0
def horloge2():
    heures = int(input('quelles heures est-il : '))
    minutes = int(input("combien de minute y'a t-il : "))
    secondes = int(input('combien de secondes avons nous : '))
    alarmes_heures = int(input("l'heure de l'alarme : "))
    alarmes_minutes = int(input("les minutes de l'alarme : "))
    alarmes_secondes = int(input("les secondes de l'alarme : "))
    while heures < 12:
            while minutes < 60:
                    while secondes < 60:
                        if heures == alarmes_heures:
                            if minutes == alarmes_minutes:
                                if secondes == alarmes_secondes:
                                    print("bip bip bip")
                        print(heures, ':', minutes, ':', secondes, "AM")
                        time.sleep(1)
                        secondes=secondes+1
                    secondes=0
                    minutes=minutes+1
            heures=heures+1
            minutes=0

    while heures < 24:
        while minutes < 60:
            while secondes < 60:
                if heures == alarmes_heures and minutes == alarmes_minutes and secondes == alarmes_secondes:
                    print("Bip bip bip")
                heures_12h = heures - 12 if heures > 12 else heures
                alarmes_heures_12h = alarmes_heures - 12 if alarmes_heures > 12 else alarmes_heures
                print(heures_12h, ':', minutes, ':', secondes, "PM")
                time.sleep(1)
                secondes = secondes + 1
            secondes = 0
            minutes = minutes + 1
        heures = heures + 1
        minutes = 0



while True:
    heures = input("Veuillez choisir un modèle d'heure soit 24h soit 12h (AM or PM): ")
    if heures == "24h":
        horloge()
        break
    elif heures == "12h":
        horloge2()
        break
    else:
        print("Format d'heure invalide. Veuillez choisir soit 24h soit 12h.")