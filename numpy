import numpy as np
ar=[1.9,1.7,1.8]
ar2=[60,50,90]
np_weight=np.array(ar)
np_height=np.array(ar2)
print(np.logical_and(np_weight>1.8, np_height>60))
print(np.logical_or(np_weight>1.8, np_height>60))
tog=np.array([np_height, np_weight])
for x in np.nditer(tog):
    print(x)
print(np.random.rand())
coin = np.random.randint(0,2)
print(coin)
np.random.seed(123)
