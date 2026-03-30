
import matplotlib.pyplot as plt
import numpy as np

categories =np.array(["Grains", "Fruit", 'Protein', 'Sweets', 'Vegetables' ])

values =np.array([100, 120, 300, 20, 250])

plt.bar(categories, values, color = 'green')
plt.title('How much do you need to eat of each one?', fontsize = 15)
plt.xlabel('Foods', fontsize= 20)


plt.show()  
plt.barh(categories, values, color = 'green')
plt.title('How much do you need to eat of each one?', fontsize = 15)
plt.xlabel('Foods')


plt.show()  


