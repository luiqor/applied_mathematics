import matplotlib.pyplot as plt
import numpy as np
import matplotlib.axes

t = np.linspace(-np.pi , np.pi, 10000)
x= np.log(np.tan(t))
y= 1/ (np.cos(t)**2)
# x= 5*np.sin(2*t)
# y= 10*np.cos(2*t)
#що таке ln, чи правильно я його задала - правильно, вкажи в лабі що log це для натурального як раз

plt.figure(figsize=(9, 9))
plt.plot(x, y,"g")
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Параметрично задана крива')
plt.legend(['y= 1/ ((np.cos(t))**2), x= np.log(np.tan(t))'], loc='upper center')
plt.axis([-10, 10, -2, 15])
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.show()