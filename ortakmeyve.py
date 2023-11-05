meyveler = ["elma", "muz", "portakal", "çilek", "karpuz", "üzüm"]

meyveler2 = ["muz", "mango", "kavun", "kiraz", "şeftali", "portakal"]

ortak_meyveler = []

for ortak_meyve in meyveler:
    if ortak_meyve in meyveler2:
        ortak_meyveler.append(ortak_meyve)

print("Ortak meyveler:", ortak_meyveler)
