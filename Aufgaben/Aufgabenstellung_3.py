# Jacobi-Verfahren
"""
Aufgabenstellung
2x1 − 1x2 = 3
−x1 + 2x2 − 1x3 = 4
−x2 + 2x3 = 5
Startvektor (2,2,2)
"""


import numpy as np

A = np.array([[2, -1, 0],
              [-1, 2, -1],
              [0, -2, 2]])

b = np.array([[3, 4, 5]])
b = b.T
x = np. array([[2, 2, 2]]) # Startvektor
x = x.T
anzahl_schritte = 50 # Hier kann die Anzahl der zu durchlaufenden Schritte angegeben werden. Wenn gewünscht ändern.
i = 0

#print('A= \n', A ,'\n')
#print('b= \n', b ,'\n')

# Aufteilen von A in L, D und R

# D und D_inverse
D = np.diag(np.diag(A)) # Diagonale, alles andere 0
#print('D= \n', D ,'\n')
D_inverse = np.linalg.inv(D)
#print('D_inverse= \n', D_inverse ,'\n')

# L
L = np.tril(A, -1) # tril gibt das untere (lower) Dreieck der Matrize aus. -1 legt die Funktion eine Diagonale unter die Hauptdiagonale
#print('L= \n', L ,'\n')

# R
R = np.triu(A, 1) # triu gibt das obere (upper) Dreieck der Matrize aus. 1 legt die Funktion eine Diagonale über die Hauptdiagonale
#print('R= \n', R ,'\n')

while (i < anzahl_schritte):
    # x = (-D_inverse * ((L + R) * x - b))
    y = np.dot((L + R), x) # Matrix-Vektor-Produkt von L +R und x
    z = y - b # b vom zwischenergebnis Abziehen
    x = np.dot(-D_inverse, z) # Matrix-Vektor-Produkt von der negativen Matrix D_inverse und dem Vektor z
    i = i + 1
print('Die Lösung des Gleichungssystems ist x= \n \n', x, '\n')
print('Es wurden', anzahl_schritte, 'Schritte durchlaufen.')



