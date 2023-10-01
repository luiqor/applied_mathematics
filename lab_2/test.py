import matplotlib.pyplot as plt
import numpy as np

# Number of bars in the histogram
num_bars = 70

# Generate random data for the histogram
data = np.random.randn(1000)

# Generate a list of unique random colors
colors = [plt.cm.viridis(np.random.rand()) for _ in range(num_bars)]

# Create a figure and axis
fig, ax = plt.subplots()

# Create individual bar plots with unique colors
for i in range(num_bars):
    ax.hist(data, bins=30, color=colors[i], alpha=0.7, label=f'Bar {i+1}', edgecolor='black')

# Add labels and title
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.set_title('Random Histogram with 70 Unique Color Bars')

# Add a legend
ax.legend()

# Show the plot
plt.show()