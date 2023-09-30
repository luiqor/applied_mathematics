import matplotlib.pyplot as plt
import numpy as np
#лекція 5 Контурні графіки.
x=np.linspace(-10,10,60)
y=np.linspace(-10,10,60)
x,y =np.meshgrid(x, y)
equation = 4 * x**2 - 4 * x * y + y**2 - 15

plt.contour(x,y,equation, levels=[0], colors="magenta")
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Кольорова задана крива')
plt.legend(['4 * x**2 - 4 * x * y + y**2 - 15 = 0'])

plt.show()