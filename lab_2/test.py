import numpy as np
from matplotlib import pyplot as plt
x = np.random.randn(700)
n, bins, patches = plt.hist(x, bins=70, color='red', rwidth=0.8, label = 'стовпчики')
col = (n-n.min())/(n.max()-n.min())
cm = plt.cm.get_cmap('hsv')
for c, p in zip(col, patches):
   plt.setp(p, 'facecolor', cm(c))

plt.legend()
plt.title('Гісторграма matplotlib',
          fontweight = "bold")
plt.xlabel("bins") 
plt.ylabel("n")
plt.show()