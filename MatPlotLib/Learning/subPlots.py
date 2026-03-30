import matplotlib.pyplot as plt
import numpy as np

#figure = canvas
#axis = subplot
x = np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5])
figure, axes = plt.subplots(3, 2 )
axes[1,0].plot(x, x*2, color = 'red')
axes[2,0].plot(x, x**2, color = 'red')
axes[1,1].plot(x, x**3, color = 'red')
axes[2,1].graph(x, x**4, color = 'red')

axes[1,0].set_title('linear', fontsize = 20)
axes[2,0].set_title('quadratic', fontsize = 20)
axes[1,1].set_title('cubic', fontsize = 20)
axes[2,1].set_title('quartic', fontsize = 20)

plt.tight_layout()
plt.show()