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

horloge()