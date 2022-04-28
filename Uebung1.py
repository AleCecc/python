
import numpy as np
np.random.seed(0)

from sklearn import datasets

import matplotlib.pyplot as plt

X, Y= datasets.make_blobs(n_samples=1000, n_features=2, centers=2, random_state=7)
plt.scatter(*X.T, c=Y)
