import numpy as np
import pandas as pd
from scipy.stats import gaussian_kde

def compute_kde_difference_auc(Xy, columns, names): 
    trapzs = pd.DataFrame(columns=columns, index=names[2:])
    for column in columns:
            mins = [X[column].min() for X,_ in Xy]
            maxs = [X[column].max() for X,_ in Xy]
            grid = np.linspace(np.min(mins), np.max(maxs), 501) 

            kdes = [gaussian_kde(X[column]) for X,_ in Xy]
            aucs = np.zeros(len(Xy) - 1)
            
            baseline = kdes[0]
            for i in range(1, len(Xy)):
                kde_i = kdes[i]
                diff = np.abs(kde_i(grid) - baseline(grid))
                aucs[i-1] = np.trapz(diff, grid)

            trapzs[column] = aucs

    return trapzs