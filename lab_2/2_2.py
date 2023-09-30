import matplotlib.pyplot as plt
import numpy as np
fi = np.linspace(0, 2 * np.pi, 1000)
ro = 3 / (1+ 2 * np.cos(fi))

plt.figure(figsize=(9, 9))
plt.polar(fi, ro, "r")
plt.title('Крива другого порядку в полярній системі координат', fontsize=14)
plt.grid(True)

plt.show()