import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
np.random.seed(200)
x = np.random.randn(700, 3)
   
colors = ['orange', 'purple', 'lime']
#colors = plt.clim (vmin = 'r', vmax = 'blue')
 
plt.hist(x, bins = 70,
         color = colors,
         label = colors)
 
plt.legend()
 
plt.title('Гісторграма matplotlib',
          fontweight = "bold")

plt.show()

# гістограми у 6 лекції Z