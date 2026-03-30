import matplotlib.pyplot as plt
import numpy as np


scores = np.random.normal(loc= 70, scale = 10, size= 1000000)
scores= np.clip(scores, 0, 100)

plt.hist(scores, bins=1000)
plt.xlabel('notas')
plt.ylabel('cantidad de alumnos')

plt.show() 