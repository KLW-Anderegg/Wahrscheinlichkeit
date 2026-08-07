n = 1 #Anzahl Personen
p = 365/365  #Wkeit, dass alle unterschiedliche Geburtstage haben

while p > 0.5:
    p = p * (365-n) / 365
    n += 1

print("bei ", n, " Personen ist die Wahrscheinlichkeit,")
print("dass mindestens zwei Personen den gleichen")
print("Geburtstag haben, erstmals >50%")
print("Die Wahrscheinlichkeit ist dann ", 1-p)