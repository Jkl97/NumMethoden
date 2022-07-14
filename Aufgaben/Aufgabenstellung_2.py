# Gradientenabstiegsverfahren
import matplotlib.pyplot as plt

x = [-1, 0, 1.5, 3, 3.5, 4, 4.5, 6, 7.3]
y = [-0.5, 0.5, 1.8, 2, 4, 4.3, 5, 6.8, 7]

toleranz = 0.001
learning_rate = 0.001
a1 = 0
a2 = 0
n = len(x)
za1 = 0
za2 = 0
delta1 = 5
delta2 = 5
z = []

def fegradienta1(y, x, a1, a2): return (-2*x * (y- (a1*x + a2))) # Funktion einzelner Gradient a1
def fegradienta2(y, x, a1, a2) : return  (-2* (y-(a1*x + a2))) # Funktion einzelner Gradient a2
def r(x, a1, a2): return a1 * x + a2 # Regressionsfunktion

# a1

while (za1 < 100 )  and (abs(delta1) > toleranz): # führe aus, solange die Änderung größer als die Toleranz ist und keine 100 Schritte gemacht wurden
    gradienta1 = 0
    for i in range(n):  # Summe Gradienten für alle y bilden
        k = fegradienta1(y[i], x[i], a1, a2)
        gradienta1 = gradienta1 + k
    delta1 = (gradienta1 * learning_rate)
    a1 = a1 - delta1
    za1= za1 +1
print('a1 beträgt:', a1)

# a2

while (za2 < 100 )  and (abs(delta2) > toleranz): # führe aus, solange die Änderung größer als die Toleranz ist und keine 100 Schritte gemacht wurden
    gradienta2 = 0
    for i in range(n):  # Summe Gradienten für alle y bilden
        k = fegradienta2(y[i], x[i], a1, a2)
        gradienta2 = gradienta2 + k
    delta2 = (gradienta2 * learning_rate)
    a2 = a2 - delta2
    za2= za2 +1
print('a2 beträgt:', a2)
print('Die gesuchte Regressionsfunktion r(x) entspricht also: r(x)=', round(a1, 4), '* x +', round(a2, 4))


for i in range(n): # erstellen einer Werteliste für r
    b = r(x[i], a1, a2)
    z.append(b)


plt.figure(figsize=(10, 10)) # plotten von Punkten und Funktion
plt.plot(x, y, "b.")
plt.plot(x, z, "r-", linewidth = 2)
plt.axis([-2, 10, -2, 10])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("vorgegebene Punkte und gefundene Regressionsfunktion")
plt.show()