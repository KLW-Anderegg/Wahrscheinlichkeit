from scipy.stats import binom

n = 100
p = 0.5
q = 1-p

pp = 0.4 #Wkeit der gefaelschten Münze


beta = 1

while beta > 0.01:
    mu = n*p
    sigma = sqrt(n*p*q)
    linkeGrenze = round(mu - 1.64*sigma,0)
    rechteGrenze = round(mu + 1.64*sigma, 0)
    beta = binom.cdf(rechteGrenze, n, pp) - binom.cdf(linkeGrenze-1, n, pp)
    print(f"bei {n} Versuchen ist Beta={beta}")
    n+=1