# Since 8.8 + sqrt(square(x)  + square(y)) = sqrt(square(10.2 - x) + square(y))
# Square the expression -> square(8.8) + square(x) + square(y) + 2 * 8.8 * sqrt(square(x) + square(y)) = square(10.2 - x) + square(y)
# Conclude that 2 * 8.8 * sqrt(square(x) + square(y)) = square(10.2) - square(8.8) - 2 * 10.2 * x
# Finally we got        square(x) + square(y) = square( (13.3 - 10.2 * x) / 8.8 )
# -> y = +/- sqrt( square( (13.3 -  10.2 * x) / 8.8 ) - square( x * x) )  
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

low_bound = -10
high_bound = 20

x = np.arange(low_bound, high_bound, 0.01)

tmp = (13.3 - 10.2 * x) / 8.8 # square(x) + square(y) = square(tmp)
final_y = tmp * tmp - x * x
y_pos = np.sqrt(np.abs(final_y))
y_neg = np.sqrt(np.abs(final_y)) * -1

plt.plot(x, y_pos)
plt.plot(x, y_neg)
plt.show()