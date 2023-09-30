import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)
y1 = np.linspace(-5, 5, 400)

X, Y = np.meshgrid(x, y1)
equation = X**2 / 20 + Y**2 / 5 - 1

y2 = (6-12*x)/5

plt.figure(figsize=(9, 9))
plt.title("Залежності: ") 
plt.xlabel("x") 
plt.ylabel("y1, y2")
plt.grid()
plt.plot(x, y2, color = "g")
plt.contour(X,Y,equation, levels=[0], colors="magenta", label='Contour Label')
# oval=... + oval.collections[0].set_label('X**2 / 20 + Y**2 / 5 - 1 = 1')

custom_legend_plot = [plt.Line2D([0], [0], color='g', lw=1.4, label='y2 = (6-12*x)/5')]
custom_legend_contour = [plt.Line2D([0], [0], color='magenta', lw=1.4, label='X**2 / 20 + Y**2 / 5 - 1 = 1')]
plt.legend(handles=custom_legend_contour + custom_legend_plot)

plt.grid(True)
plt.show()