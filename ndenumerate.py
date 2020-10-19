import numpy as np
my_array=np.zeros(shape=(5,6))
for (i,j), x in np.ndenumerate(my_array):
    print(i,j,x, sep=";")
