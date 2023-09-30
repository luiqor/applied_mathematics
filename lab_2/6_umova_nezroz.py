import matplotlib.pyplot as plt
import numpy as np
cat_par = [f"P{i}" for i in range(7)]
g1 = [31, 32, 32, 30, 32, 23, 0]
g2 = [7, 8, 9, 10, 11, 12, 13]
width = 0.2
x = np.arange(len(cat_par))
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, g1, width, label='кількість груп')
rects2 = ax.bar(x + width/2, g2, width, label='2 варіант+ 5')
ax.set_title('Групова діаграма')
ax.set_xticks(x)
ax.set_xticklabels(cat_par)
ax.legend()

#ще потрібно за колір розібратися, і наприклад якщо 3 стовпчики. А ще умова якась незроз 
plt.show()

# гістограми у 6 лекції , не те я зробила 