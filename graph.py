import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 1000, endpoint=True)

y = (50*x**2 + 10*x + 5)
y_1 = ((-5)*x**2 + 46*x)


plt.plot(x, y)
plt.plot(x, y_1)
plt.grid()
plt.show()