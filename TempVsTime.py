'''
This is a program for measuring temperature over time, used to measure
how the peltier temperatures changed over time
'''
from __future__ import division
from xlrd import open_workbook
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as cm

def obj_array(x):
    sh = wb.sheet_by_index(0)
    nested_list = [sh.row_values(i) for i in range(sh.nrows)]
    return np.array(nested_list,dtype=object)

#fill in an excel workbook here, with time in the first column and temperatures in the second
wb = open_workbook('file here') 

X=0
TEMP=1
x_data=arr[:,TEMP].astype(float)

y_data=arr[:,X].astype(float)

plt.plot(y_data,x_data,color='black')
'''plt.scatter(y_data,x_data,c=y_data,vmin=min(y_data),vmax=max(y_data))
for i in range(0,len(y_data)):
    plt.text(y_data[i],x_data[i]+.5, '%d' % (y_data[i]))'''
    
plt.ylabel('Temperature (C)')
plt.xlabel('Time')

#plt.colorbar()

plt.show()

