import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 50)
y1 = np.sqrt((1-(x**2/20))*5)
y2 = (6-12*x)/5

plt.title("Залежності: ") 
plt.xlabel("x") 
plt.ylabel("y1, y2")
plt.grid()
plt.plot(x, y1, label='y1 = np.sqrt((1-(x**2/20))*5)')
plt.plot(x, y2, label='y2 = (6-12*x)/5')
plt.legend()
plt.show()