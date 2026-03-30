import matplotlib.pyplot as plt
import numpy as np
x = np.array([2021, 2022, 2023, 2024, 2025])
sypmax = np.array([4808.93, 4818.62, 4793.30, 6099.97, 6754.49])
sypmin =np.array([3662.71, 3577.03, 3808.10, 4682.11, 4835.04])
sypmed =np.array([4273.41, 4098.93, 4450.57, 5432.78, 6125.36])

line2_style = dict(marker = '*', 
                    mfc = 'yellow',
                    markersize = 15,
                    linewidth = 4,
                    ) 

plt.plot(x,sypmax, marker = '.', 
                    mfc = 'blue',
                    markersize = 10,
                    linewidth = 2,
                    color = 'violet')
plt.plot(x,sypmin, color = 'orange', **line2_style)
plt.plot(x,sypmed,  **line2_style, color = 'green')


plt.title('Syp500 durante los años 2021-2025', fontsize= 15, family = 'arial')
plt.xlabel('Year', fontsize=20, family= 'arial')
plt.ylabel('Syp500 price', fontsize=20, family= 'arial')
plt.grid(axis='y',
         linewidth=2,
         linestyle  = 'dashed')
plt.xticks(x)
plt.show()

