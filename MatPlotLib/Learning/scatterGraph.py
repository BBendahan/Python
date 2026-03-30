import matplotlib.pyplot as plt
import numpy as np


hours_studied = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
test_scores = np.array([20, 30, 32, 45, 65, 70, 70, 80, 95, 100, 100])


hours_studied2 = np.array([0, 1, 1, 2, 4, 4, 6, 7, 8, 10, 10])
test_scores2 = np.array([20, 35, 35, 40, 76, 80, 85, 90, 95, 95, 100])


plt.scatter(hours_studied, test_scores, color = 'skyblue', alpha= 0.5, s= 200, label = 'mañana ')

plt.scatter(hours_studied2, test_scores2, color = 'red', alpha= 1, s= 200, label = 'tarde')
plt.xlabel('hours studied:', fontsize = 20)
plt.ylabel('test score:', fontsize = 20)

plt.legend()
plt.show()