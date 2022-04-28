import numpy as np
ar=[1.9,1.7,1.8]
ar2=[60,50,90]
np_weight=np.array(ar)
np_height=np.array(ar2)
bmi=np_weight/np_height**2
print(bmi)
