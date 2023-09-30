import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0 , np.pi * 2 ,200)
y= 1/ ((np.cos(t))**2)
x= np.log10(t) * np.tan(t)

plt.figure(figsize=(9, 9))
plt.plot(x, y, "g")
plt.grid(True)

plt.show()