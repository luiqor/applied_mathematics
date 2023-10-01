import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(np.pi , np.pi*2, 2000)
y= 1/ ((np.cos(t))**2)
x= np.log(np.tan(t))
#що таке ln, чи правильно я його задала - правильно, вкажи в лабі що log це для натурального як раз

plt.figure(figsize=(9, 9))
plt.plot(x, y,"g")
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Параметрично задана крива')
plt.legend(['y= 1/ ((np.cos(t))**2), x= np.log(np.tan(t))'], loc='upper center')

plt.show()