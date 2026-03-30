import matplotlib.pyplot as plt
import numpy as np



categories = np.array(['freshmen', 'sophomores', 'juniors', 'seniors'])
values = np.array([400, 250, 120, 80])
colors = ['#FFFFeF', 'yellow', 'orange', 'red']
plt.pie(values, labels= categories, autopct= '%1.1f%%', colors = colors, explode= [0,0,0,0],shadow=True, startangle=90)
plt.title("Facultad de Ingenieria de la UBA", fontsize = 15)
plt.show()