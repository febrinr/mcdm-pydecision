import numpy as np

from pyDecision.algorithm import ahp_method

weight_derivation = 'geometric'  # 'mean'; 'geometric' or 'max_eigen'

dataset = np.array([
    # g1     g2     g3     g4     g5     g6     g7
    [1, 1 / 3, 1 / 5, 1, 1 / 4, 1 / 2, 3],  # g1
    [3, 1, 1 / 2, 2, 1 / 3, 3, 3],  # g2
    [5, 2, 1, 4, 5, 6, 5],  # g3
    [1, 1 / 2, 1 / 4, 1, 1 / 4, 1, 2],  # g4
    [4, 3, 1 / 5, 4, 1, 3, 2],  # g5
    [2, 1 / 3, 1 / 6, 1, 1 / 3, 1, 1 / 3],  # g6
    [1 / 3, 1 / 3, 1 / 5, 1 / 2, 1 / 2, 3, 1]  # g7
])

weights, rc = ahp_method(dataset, wd=weight_derivation)

for i in range(0, weights.shape[0]):
    print('w(g' + str(i + 1) + '): ', round(weights[i], 3))

print('RC: ' + str(round(rc, 2)))

if rc > 0.10:
    print('The solution is inconsistent, the pairwise comparisons must be reviewed')
else:
    print('The solution is consistent')
