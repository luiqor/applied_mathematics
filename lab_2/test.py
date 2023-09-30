import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)
y1 = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y1)
equation = X**2 / 20 + Y**2 / 5 - 1

y2 = (6-12*x)/5

plt.title("Залежності: ") 
plt.xlabel("x") 
plt.ylabel("y1, y2")
plt.grid()
plt.plot(x, y2, label='y2 = (6-12*x)/5')
plt.legend()

plt.contour(X,Y,equation, levels=[0], colors="magenta")
plt.grid(True)

plt.show()