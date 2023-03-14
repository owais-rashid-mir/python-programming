# Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
# Most of the Matplotlib utilities lies under the pyplot submodule

# Drawing a line in a diagram from position (0,0) to position (6,250)
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)      # # plot() function draws a line from point to point.
plt.show()


# Output:
# We'll get an upward slope line starting from origin.