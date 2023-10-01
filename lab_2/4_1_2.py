import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,60)
y1= (x**2 - 1) / x
y2=np.cos(x)

plt.figure(figsize=(9, 9))
plt.subplot(1, 2, 1)
plt.plot(x, y1, "g")
plt.grid(True)


plt.subplot(1, 2, 2)
plt.plot(x, y2, "black")
plt.grid(True) 


plt.show()

#https://stackoverflow.com/questions/13865200/attempting-to-draw-hyperbola-in-matplotlib-produces-line-along-vertical-asymptot