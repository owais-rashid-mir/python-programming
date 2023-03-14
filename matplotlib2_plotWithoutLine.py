import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o') # To plot only the markers or points, we use shortcut string notation
                                # parameter 'o', which means 'rings'.
plt.show()