###!/usr/bin/python
### -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model, datasets
import math


X= np.array([[0],[1],[2],[3],[40],[50],[60],[70]])

Y= np.array([0,0,0,0,1,1,1,1])

logreg = linear_model.LogisticRegression()

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

Z = logreg.predict(X)

print(Z-Y)
teta0 = logreg.intercept_;
teta1 = logreg.coef_[0];
h = 1/(1 + np.exp(-teta0 -teta1*X))
plt.xlabel('X')
plt.ylabel('h')
plt.plot(h,'o')
plt.show()

