import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
np.random.seed(200)
x = np.random.randn(700, 4)
   
colors = ['orange', 'purple', 'lime', 'cyan']
#colors = plt.clim (vmin = 'r', vmax = 'blue')
 
n, bins, patches = plt.hist(x, bins = 70,
                    color = colors,
                    label = ['один', 'два', 'три','три'])
 

plt.legend()
 
plt.title('Гісторграма matplotlib',
          fontweight = "bold")

plt.show()