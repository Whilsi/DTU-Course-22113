#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x_vals = np.linspace(0,1,100)

plt.figure(figsize=(7.5,5))
plt.plot(x_vals,x_vals,label='linear')
plt.plot(x_vals,x_vals**2,label='quadratic')
plt.plot(x_vals,x_vals**3,label='cubic')
plt.legend()
plt.show()
