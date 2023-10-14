import matplotlib.pyplot as plt
import numpy as np
import matplotlib.axes as ax
theta = np.linspace(-np.pi, np.pi, 5000)
ro = 3 / (1+ 2 * np.cos(theta))
# ro2 = -3 / (1+ 2 * -np.cos(theta))

plt.figure(figsize=(6, 6))
plt.polar(theta, ro, "r", label='ro = 3 / (1+ 2 * np.cos(fi))')
plt.title('Крива другого порядку в полярній системі координат', fontsize=14)
plt.legend()
ax=plt.gca()
ax.set_rlim(0,50)
# plt.ylim(min(theta), max(theta*10))

plt.show()

#https://stackoverflow.com/questions/23205990/graph-for-a-polar-equation-is-incomplete-in-matplotlib
#https://matplotlib.org/stable/api/projections/polar.html