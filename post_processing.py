import os
import math
import numpy as np
import sys
from _pytest import mark
#from typing import List
import operator
import matplotlib.pyplot as plt

dir = "/cfdfile2/data/fm/alireza/EcoFlow/reed_channel/simulation/reed_nozzle_yarn/post_processing_point9_20mbar_v70-a6.23_b9.87_y-8.02_z12.03"
os.chdir(dir)
current_direct= os.getcwd()

# lines=f.read().splitlines()

with open("test_sort.txt", "r") as f:
    lst = [float(x) for x in f.read().split()]

list_1 = [None] *28800

for i in range(0,28800,1):
    list_1[i] = lst[0 + 13 * i:13 + 13 * i]
#print (list_1 [0][2])


sort_1 = sorted(list_1, key=operator.itemgetter(0))


#x_coordinate_f=(C(:,1)-0.00105);
#p_f_x=C(:, 4);
#p_f_y=C(:, 5);
#p_f_z=C(:, 6);
#v_f_x=C(:,7);
#v_f_y=C(:,8);
#v_f_z=C(:,9);

x_cord = np.zeros(28800)
p_f_x=np.zeros(28800)
p_f_y=np.zeros(28800)
p_f_z=np.zeros(28800)
v_f_x=np.zeros(28800)
v_f_y=np.zeros(28800)
v_f_z=np.zeros(28800)


for j in range(0,28800):
    x_cord[j] = (sort_1[j][0]-0.00105)*1000
    p_f_x[j] = sort_1[j][3]
    p_f_y[j] = sort_1[j][4]
    p_f_z[j] = sort_1[j][5]
    v_f_x[j] = sort_1[j][6]
    v_f_y[j] = sort_1[j][7]
    v_f_z[j] = sort_1[j][8]

#x = np.sum(x_cord)/5
#print (x)
#print (sort_1[0][8])
#print (p_f_z)

x_cord_2 = np.zeros(720)
pressure_force_x = np.zeros(720)
pressure_force_y = np.zeros(720)
pressure_force_z = np.zeros(720)
viscous_force_x = np.zeros(720)
viscous_force_y = np.zeros(720)
viscous_force_z = np.zeros(720)


for kk in range(0,720):
    y=40*kk
    z=40*(kk+1)
    x_cord_2 [kk] = np.sum(x_cord[y:z])/40
    pressure_force_x[kk] = np.sum(p_f_x[y:z])
    pressure_force_y[kk] = np.sum(p_f_y[y:z])
    pressure_force_z[kk] = np.sum(p_f_z[y:z])

    viscous_force_x[kk] = np.sum(v_f_x[y:z])
    viscous_force_y[kk] = np.sum(v_f_y[y:z])
    viscous_force_z[kk] = np.sum(v_f_z[y:z])

#print(x_cord_2)


f_x = pressure_force_x+viscous_force_x
f_y = pressure_force_y+viscous_force_y
f_z = pressure_force_z+viscous_force_z
f_0 = np.zeros(720)

total_force_x = sum(f_x)
total_pressure_force_x = sum(pressure_force_x)
total_viscous_force_x = sum(viscous_force_x)

total_force_y = sum(f_y)
total_pressure_force_y = sum(pressure_force_y)
total_viscous_force_y = sum(viscous_force_y)

total_force_z = sum(f_z)
total_pressure_force_z = sum(pressure_force_z)
total_viscous_force_z = sum(viscous_force_z)


net_force = open("ne_force_test.txt","w")
net_force.write("Forces components: Fx, Fy, Fz \n")
net_force.write("Viscous Forces:"+str(total_viscous_force_x) +","+str(total_viscous_force_y) +","+str(total_viscous_force_z)+" \n")
net_force.write("Pressure Forces:"+str(total_pressure_force_x) +","+str(total_pressure_force_y) +","+str(total_pressure_force_z)+" \n")
net_force.write("Net Forces:"+str(total_force_x) +","+str(total_force_y) +","+str(total_force_z)+" \n")
net_force.close()

plt.figure()
plt.plot(x_cord_2, 10**7*f_x, 'g-.', label='Fx')
plt.plot(x_cord_2, 10**7*f_y, 'b-', label='Fy')
plt.plot(x_cord_2, -1*10**7*f_z, 'k-', label='-Fz')
plt.plot(x_cord_2, f_0 ,'r-.', label='F=0')

plt.title('Force along the yarn')
plt.xlabel('x (mm)')
plt.ylabel('Force/L (mN/m)')
plt.legend(loc='best')
pic_name= "5.png"
plt.savefig(pic_name, transparent=False)
#plt.show()
plt.close()

