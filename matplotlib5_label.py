import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data", loc = 'left')  # title at top of graph
plt.xlabel("Average Pulse")     # label for x-axis
plt.ylabel("Calorie Burnage")   # label for y-axis

plt.show()