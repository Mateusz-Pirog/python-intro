from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm import normalizations
from pymcdm.helpers import rankdata
import numpy as np
import pandas as pd

# Dane wejściowe
decision_matrix = np.array([
    [50000, 200000, 0.1, 12],
    [45000, 180000, 0.2, 10],
    [55000, 220000, 0.15, 14],
    [47000, 210000, 0.1, 11]
])

weights = np.array([0.3, 0.4, 0.2, 0.1])
types = np.array([-1, 1, -1, -1])  # -1: minimalizacja, 1: maksymalizacja

# Normalizacja (dla TOPSIS)
norm_matrix = normalizations.minmax_normalization(decision_matrix, ['min', 'max', 'min', 'min'])

# TOPSIS
topsis = TOPSIS()
topsis_scores = topsis(decision_matrix, weights, types)
topsis_ranking = rankdata(topsis_scores, reverse=True)

# SPOTIS
bounds = [
    [45000, 55000],
    [180000, 220000],
    [0.1, 0.2],
    [10, 14]
]

spotis = SPOTIS(bounds)
spotis_scores = spotis(decision_matrix, weights, types)
spotis_ranking = rankdata(spotis_scores, reverse=False)

# Wyniki
alternatives = ['A1', 'A2', 'A3', 'A4']
results_df = pd.DataFrame({
    'Alternative': alternatives,
    'TOPSIS Score': topsis_scores,
    'TOPSIS Rank': topsis_ranking,
    'SPOTIS Score': spotis_scores,
    'SPOTIS Rank': spotis_ranking
})

results_df.to_csv('wyniki_mcdm.csv', index=False)
print(results_df)
