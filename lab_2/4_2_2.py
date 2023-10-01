import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,60)
y1= (x**2 - 1) / x
y2=np.cos(x)

plt.figure(figsize=(9, 9))

plt.subplot(1, 2, 1)
plt.plot(x, y1, "g", linewidth=3)
plt.title('Графік f(x) = (x^2 - 1) / x')
plt.xlabel('x')
plt.ylabel('y1')
plt.grid(True)
plt.legend(['y1 = (x^2 - 1) / x'])
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.subplot(1, 2, 2)
plt.plot(x, y2, "black", linewidth=1)
plt.title('Графік f(x) = cos(x)')
plt.xlabel('x')
plt.ylabel('y2')
plt.grid(True) 
plt.legend(['y2 = cos(x)'],loc='upper right')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.tight_layout(pad=3)
plt.show()