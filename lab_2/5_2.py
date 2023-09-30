import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 500)
y1=np.linspace(-10,10,60)
x,y1 =np.meshgrid(x, y1)
equation = (x**2/20)+(y1**2/5)

plt.contour(x,y1,equation, levels=[1], colors="magenta")

# y= (x**2/20)+(y**2/5)=1
# y1_neg = -(np.sqrt((1-(x**2/20))*5))
y2 = (6-12*x)/5

plt.title("Залежності: ") 
plt.xlabel("x") 
plt.ylabel("y1, y2")
plt.grid()
plt.plot(x, y1, label='y1 = np.sqrt((1-(x**2/20))*5)')
plt.plot(x, y2, label='y2 = (6-12*x)/5')
plt.legend()

plt.show()
#неявно задана функція пошукати