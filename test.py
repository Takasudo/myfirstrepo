import numpy as np
import matplotlib.pyplot as plt

values = np.random.normal(0,1.0,100000)

plt.hist(values,50)
plt.show()
