import numpy as np
import pandas as pd

# Graine fixe : même jeu de données pour toute la promotion
rng = np.random.default_rng(7)

# Nombre de transactions
n = 5000

# Génération des variables
montant = np.round(rng.lognormal(6.2, 1.1, n), 2)  # Beaucoup de petits montants
anciennete = rng.integers(0, 120, n)               # Ancienneté du client en mois
freq = rng.poisson(3, n) + 1                       # Transactions sur 24 h
nuit = rng.binomial(1, 0.18, n)                    # Paiement entre 0 h et 5 h

# Calcul du score et détermination de la fraude (0 ou 1)
score = 2.2 * (np.log10(montant) - 3.0) - anciennete / 60 + (freq - 3) / 3 + nuit * 1.2
fraude = ((score + rng.normal(0, 0.35, n)) > 0.6).astype(int)

# Création du DataFrame
df = pd.DataFrame({
    'montant': montant,
    'anciennete': anciennete,
    'freq_24h': freq,
    'nuit': nuit,
    'fraude': fraude
})

# Export en CSV
df.to_csv('data/transactions.csv', index=False)

print('data/transactions.csv écrit :', n, 'lignes,', fraude.sum(), 'fraudes')