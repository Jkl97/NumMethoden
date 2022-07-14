# Bisektionsverfahren und Fixpunktiteration
import math

def f ( x ):    return (math.log((2 + 4 * x**2 )) -x)

rechenart = input('Gebe die Rechenart an "b" für Bisektionsverfahren oder "f" für Fixpunktiteration:')

if (rechenart == 'b'):
    print('Das Bisektionsverfahren wurde ausgewählt.')

    # Bisektionsverfahren
    toleranz = 0.001
    a = 0
    b = 5
    fa = f(a)
    fb = f(b)
    m = 0.5 * (a + b)
    fm = f(m)
    i = 0
    if (((fa < 0) and (fb > 0)) or ((fa > 0) and (fb < 0))):# prüfen ob eine Nullstelle zwischen a und b existiert
        if((fa < 0) and (fb > 0)):  # Graph hat positive Steigung zwischen a und b
            while ((abs(a - b)) > toleranz) and (i < 100) and (abs(fm)> toleranz) and (fm != 0):  # Abbruch bei Erreichen der Toleranz, 100 Schritten oder im Fall Funktionswert = 0
                m = 0.5 * (a + b)
                fm = f(m)
                i = i + 1
                if (fm > 0):
                    b = m
                elif (fm < 0):
                    a = m
        elif ((fa > 0) and (fb < 0)):  # Graph hat negative Steigung zwischen a und b
            while ((abs(a - b)) > toleranz) and (i < 100) and (abs(fm)> toleranz) and (fm != 0):
                m = 0.5 * (a + b)
                fm = f(m)
                i = i + 1
                if (fm < 0):
                    b = m
                elif (fm > 0):
                    a = m

        #Ergebnismeldung
        print('Die Nullstelle liegt bei x=', m, 'Der Funktionswert f(x) beträgt hier:', f(m), '. Es wurden', i, 'Schritte Durchlaufen')

        #Abbruchgründe der While-Schleife
        print('Die Berechnung wurde beendet, da:')
        if (i == 100):
             print('Die Berechnung nach 100 Schritten abgebrochen wurde.')
        elif (abs(fm) < toleranz):
            print('Der Funktionswert innerhalb der Toleranz liegt.')
        elif ((abs(a - b)) > toleranz):
            print('Die Werte von a und b sich bis auf die gegebene Toleranz angenähert haben.')
    else:
        print('Geben sie andere Werte für a und b an. Es gibt nicht genau eine Nullstelle zwischen a und b.')



elif (rechenart == 'f'):
    print('Die Fixpunktiteration wurde ausgewählt.')

    #Fixpunktiteration
    def F(x):  return f(x) + x

    x = 0
    toleranz = 0.001
    i = 0
    Fx = F(x)
    fx = f(x)

    while (i < 100) and (abs(fx) > toleranz) and (fx != 0) and ((abs(fx - x)) > toleranz):
        i = i + 1
        x = F(x)
        fx = f(x)
    # Ergebnismeldung
    print('Die Nullstelle liegt bei x=', x, 'Der Funktionswert f(x) beträgt hier:', fx, '. Es wurden', i,
          'Schritte Durchlaufen')

    # Abbruchgründe der While-Schleife
    print('Die Berechnung wurde beendet, da:')
    if (i == 100):
        print('Die Berechnung nach 100 Schritten abgebrochen wurde.')
    elif (abs(fx) < toleranz):
        print('Der Funktionswert innerhalb der Toleranz liegt.')
    elif ((abs(fx - x)) > toleranz):
        print('Der Fixpunkt sich bis auf die gegebene Toleranz angenähert hat.')

else:
    print('Es ist ein Fehler aufgetreten. Bitte geben sie eine korrekte Rechenart an.')

