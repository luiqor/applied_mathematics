import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,60)
y1= (x**2 - 1) / x
y2=np.cos(x)

plt.figure(figsize=(9, 9))
plt.plot(x, y1, "g")
plt.grid(True)

plt.figure(figsize=(9, 9))
plt.plot(x, y2, "black")
plt.grid(True) 


plt.show()