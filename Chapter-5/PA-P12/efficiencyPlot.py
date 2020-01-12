import numpy as np
import matplotlib.pyplot as plt

N = 35
p = np.linspace(0, 1, 100)

ef1 = [N*i*(1-i)**(N-1)for i in p] 
ef2 = [N*i*(1-i)**(2*(N-1))for i in p]

plt.plot(p,ef1)
plt.plot(p,ef2)

plt.show()
