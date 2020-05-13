import os
import math
from math import *
from Case import Case
import sys
import numpy as np
from _pytest import mark
#from typing import List
import operator
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import operator
import array


# define the case setup
setup_1 = Case("Reed_1", 74, -8.02, 12.03, 6.23, 9.87, 1.6, 5)
setup_2= Case("Reed_2", 74, -8.02, 12.03, 6.23, 9.87, 1.6, 5)
setup_3= Case("Reed_3", 74, -8.02, 12.03, 6.23, 9.87, 1.6, 5)
setup_4= Case("Reed_4", 74, -8.02, 12.03, 6.23, 9.87, 1.6, 5)
setup_5= Case("Reed_1", 74, -8.02, 12.03, 6.23, 10.87, 1.6, 5)
setup_6= Case("Reed_1", 74, -8.02, 12.03, 6.23, 8.87, 1.6, 5)
setup_7= Case("Reed_1", 74, -8.02, 12.03, 7.23, 9.87, 1.6, 5)
setup_8= Case("Reed_1", 74, -8.02, 12.03, 5.23, 9.87, 1.6, 5)
setup_9= Case("Reed_1", 74, -8.02, 12.03, 5.607, 8.883, 1.6, 5)
setup_10= Case("Reed_1", 74, -8.02, 12.03, 6.853, 10.857, 1.6, 5)
setup_11= Case("Reed_1", 60, -8.02, 12.03, 6.23, 9.87, 1.6, 5)
setup_12= Case("Reed_1", 60, -8.02, 12.03, 6.23, 9.87, 1.5, 5)
setup_13= Case("Reed_1", 60, -8.02, 12.03, 5.607, 8.883, 1.5, 5)
setup_14= Case("Reed_1", 60, -8.02, 12.03, 6.853, 10.857, 1.5, 5)
setup_15= Case("Reed_1", 40, -8.02, 12.03, 6.23, 9.87, 1.6, 5)
setup_16= Case("Reed_1", 40, -8.02, 12.03, 6.23, 9.87, 1.3, 5)
setup_17= Case("Reed_1", 40, -8.02, 12.03, 6.23, 9.87, 1.1, 5)
setup_18= Case("Reed_1", 74, -7.11, 11.62, 5.63, 11.23, 1.6, 5)
setup_19= Case("Reed_8", 74, -8.02, 12.03, 6.23, 9.87, 1.6, 5)
setup_20= Case("Reed_8", 60, -8.02, 12.03, 6.23, 9.87, 1.6, 5)
setup_21= Case("Reed_8", 60, -7.689, 9.03, 7.603, 9.356, 1.6, 5)
setup_22= Case("Reed_8", 60, -7.689, 9.03, 6.082, 7.485, 1.6, 5)
setup_23= Case("Reed_8", 40, -7.689, 9.03, 6.082, 7.485, 1.6, 5)
setup_24= Case("Reed_8", 40, -7.689, 9.03, 6.082, 7.485, 1.3, 5)
setup_25= Case("Reed_8", 40, -7.689, 9.03, 6.082, 7.485, 1.1, 5)
setup_26 = Case("Reed_1", 74, -8.02, 12.03, 6.23, 9.87, 1.6, 3)
setup_27 = Case("Reed_1", 74, -8.02, 12.03, 6.23, 9.87, 1.9, 3)

#i=input("the setup number is: ")
i=16
# point = input("the location of the yarn is: ")
# point = 1
speed = 60

#### speed = input("the speed of the yarn is: ")

reed_type = eval("setup_"+str(i)+".reed")
interval = eval("setup_"+str(i)+".interval")
y_n = eval("setup_"+str(i)+".y_n")
z_n= eval("setup_"+str(i)+".z_n")
alpha= eval("setup_" + str(i) + ".alpha")
beta= eval("setup_" + str(i) + ".beta")
diameter= eval("setup_" + str(i) + ".n_diameter")
p_in = eval("setup_" + str(i) + ".p_in")


# f_x = np.zeros(720)
# f_y= np.zeros(720)
# f_z=np.zeros(720)
# total_force_x = np.zeros(15)
# total_force_y = np.zeros(15)
# total_force_z = np.zeros(15)

f_x = [None]*720
f_y= [None]*720
f_z=[None]*720
total_force_x = [None]*17
total_force_y = [None]*17
total_force_z = [None]*17


for point in range(1,17):
    ####### set the directory
    setup_dir = "/cfdfile2/data/fm/alireza/EcoFlow/Test_plan/setup_"+str(i)+"/setup_"+str(i)+"_yarn_position_"+str(point)+"" \
                                    "/setup_"+str(i)+"_yarn_position_"+str(point)+"_yarn_speed_"+str(speed)+""
    os.chdir(setup_dir)
    direct = os.getcwd()
    ######## Force distribution on the yarn ##############

    ### modify the file

    file_2 = open("Force_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + ".txt", "r")
    file_2_lines = file_2.readlines()
    range_file_2 = len(file_2_lines)

    force_filename = "Force_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + ".csv"
    file_force_1 = open(force_filename, "w")
    for a in range(1, len(file_2_lines)):
        file_force_1.write(file_2_lines[a])
    file_force_1.close()

    if interval == 74:
        ring_elment = 28800
    elif interval == 60:
        ring_elment = 23200
    elif interval == 40:
        ring_elment = 15200

    list_1 = [None] *ring_elment
    line_t = 0

    with open(force_filename, "r") as f:
         lst = [float(x_line) for x_line in f.read().split()]

    for jj in range(0,ring_elment,1):
         list_1[jj] = lst[0 + 13 * jj:13 + 13 * jj]

    sort_1 = sorted(list_1, key=operator.itemgetter(0))
    x_cord = np.zeros(ring_elment)
    p_f_x=np.zeros(ring_elment)
    p_f_y=np.zeros(ring_elment)
    p_f_z=np.zeros(ring_elment)
    v_f_x=np.zeros(ring_elment)
    v_f_y=np.zeros(ring_elment)
    v_f_z=np.zeros(ring_elment)
#
    for j in range(0,ring_elment):
        x_cord[j] = (sort_1[j][0]-0.00105)*1000
        p_f_x[j] = sort_1[j][3]
        p_f_y[j] = sort_1[j][4]
        p_f_z[j] = sort_1[j][5]
        v_f_x[j] = sort_1[j][6]
        v_f_y[j] = sort_1[j][7]
        v_f_z[j] = sort_1[j][8]
#
    x_cord_2 = np.zeros(ring_elment/40)
    pressure_force_x = np.zeros(ring_elment/40)
    pressure_force_y = np.zeros(ring_elment/40)
    pressure_force_z = np.zeros(ring_elment/40)
    viscous_force_x = np.zeros(ring_elment/40)
    viscous_force_y = np.zeros(ring_elment/40)
    viscous_force_z = np.zeros(ring_elment/40)
#
    for kk in range(0,ring_elment/40):
        y=40*kk
        z=40*(kk+1)
        x_cord_2 [kk] = np.sum(x_cord[y:z])/40
        pressure_force_x[kk] = np.sum(p_f_x[y:z])
        pressure_force_y[kk] = np.sum(p_f_y[y:z])
        pressure_force_z[kk] = np.sum(p_f_z[y:z])

        viscous_force_x[kk] = np.sum(v_f_x[y:z])
        viscous_force_y[kk] = np.sum(v_f_y[y:z])
        viscous_force_z[kk] = np.sum(v_f_z[y:z])

    f_x[point] = pressure_force_x + viscous_force_x
    f_y[point] = pressure_force_y + viscous_force_y
    f_z[point] = pressure_force_z + viscous_force_z


    f_0 = np.zeros(ring_elment/40)
    #
    total_force_x[point] = sum(f_x[point])
    total_force_y[point] = sum(f_y[point])
    total_force_z[point]= sum(f_z[point])

    command_remove = "rm " + force_filename + ""
    os.system(command_remove)

    ### net forces on the yarn ###

    point_dir = "/cfdfile2/data/fm/alireza/EcoFlow/Test_plan/setup_" + str(i) + "/"
    os.chdir(point_dir)
    direct = os.getcwd()

    net_force_points = open("net_force_per_lenght_point_setup_"+ str(i)+"_yarn_speed_"+str(speed)+".txt","ab+")

    net_force_points.write("point"+str(point)+" "+str(10**6*total_force_x[point]/(interval-2)) +"  "
               ""+str(10**6*total_force_y[point]/(interval-2)) +"  "+str(10**6*total_force_z[point]/(interval-2))+" \n")
    net_force_points.close()

# ###############################

### forces distribution along the yarn ###

## force components
point_dir = "/cfdfile2/data/fm/alireza/EcoFlow/Test_plan/setup_" + str(i) + "/"
os.chdir(point_dir)
direct = os.getcwd()

# yarn_position_1_5_9

plt.figure()
# plt.plot(x_cord_2[:719]/(interval-2), 10**7*f_x[1][:719], 'g-.', label='Point 1', marker="o")
plt.plot(x_cord_2/(interval-2), 10**7*f_x[1], 'g-.', label='Point 1')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[5], 'b-', label='Point 5')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[9], 'k-', label='point 9')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[16], 'm--', label='point 16')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in x direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fx_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_1_5_9_16.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()


plt.figure()
plt.plot(x_cord_2/(interval-2), 10**7*f_y[1], 'g-.', label='Point 1')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[5], 'b-', label='Point 5')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[9], 'k-', label='point 9')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[16], 'm--', label='point 16')

plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in y direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fy_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_1_5_9_16.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

plt.figure()
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[1], 'g-.', label='Point 1')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[5], 'b-', label='Point 5')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[9], 'k-', label='point 9')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[16], 'm--', label='point 16')


plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in -z direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fz_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_1_5_9_16.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

########################## yarn_position_2_6_10_13

plt.figure()
plt.plot(x_cord_2/(interval-2), 10**7*f_x[2], 'g-.', label='Point 2')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[6], 'b-', label='Point 6')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[10], 'k-', label='point 10')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[13], 'm--', label='Point 13')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in x direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fx_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_2_6_10_13.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()


plt.figure()
plt.plot(x_cord_2/(interval-2), 10**7*f_y[2], 'g-.', label='Point 2')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[6], 'b-', label='Point 6')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[10], 'k-', label='point 10')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[13], 'm--', label='point 13')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in y direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fy_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_2_6_10_13.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

plt.figure()
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[2], 'g-.', label='Point 2')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[6], 'b-', label='Point 6')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[10], 'k-', label='point 10')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[13], 'm--', label='point 13')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in -z direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fz_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_2_6_10_13.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

########################## yarn_position_3_7_11_14

plt.figure()
plt.plot(x_cord_2/(interval-2), 10**7*f_x[3], 'g-.', label='Point 3')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[7], 'b-', label='Point 7')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[11], 'k-', label='point 11')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[14], 'm--', label='point 14')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in x direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fx_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_3_7_11_14.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

plt.figure()
plt.plot(x_cord_2/(interval-2), 10**7*f_y[3], 'g-.', label='Point 3')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[7], 'b-', label='Point 7')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[11], 'k-', label='point 11')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[14], 'm--', label='point 14')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in y direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fy_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_3_7_11_14.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()



plt.figure()
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[3], 'g-.', label='Point 3')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[7], 'b-', label='Point 7')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[11], 'k-', label='point 11')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[14], 'm--', label='point 14')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in -z direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fz_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_3_7_11_14.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()


########################## yarn_position_4_8_12_15

plt.figure()
plt.plot(x_cord_2/(interval-2), 10**7*f_x[4], 'g-.', label='Point 4')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[8], 'b-', label='Point 8')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[12], 'k-', label='point 12')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[15], 'm--', label='point 15')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in x direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fx_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_4_8_12_15.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

plt.figure()
plt.plot(x_cord_2/(interval-2), 10**7*f_y[4], 'g-.', label='Point 4')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[8], 'b-', label='Point 8')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[12], 'k-', label='point 12')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[15], 'm--', label='point 15')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in y direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fy_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_4_8_12_15.png"
plt.savefig(pic_name, transparent=False)
# plt.show()

plt.close()
plt.figure()
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[4], 'g-.', label='Point 4')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[8], 'b-', label='Point 8')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[12], 'k-', label='point 12')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[15], 'm--', label='point 15')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in -z direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fz_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_4_8_12_15.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

########################## yarn_position_1_2_3_4

plt.figure()
plt.plot(x_cord_2/(interval-2), 10**7*f_x[1], 'g-.', label='Point 1')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[2], 'b-', label='Point 2')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[3], 'k-', label='point 3')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[4], 'm--', label='point 4')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in x direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fx_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_1_2_3_4.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

plt.figure()
plt.plot(x_cord_2/(interval-2), 10**7*f_y[1], 'g-.', label='Point 1')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[2], 'b-', label='Point 2')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[3], 'k-', label='point 3')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[4], 'm--', label='point 4')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in y direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fy_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_1_2_3_4.png"
plt.savefig(pic_name, transparent=False)
# plt.show()

plt.close()
plt.figure()
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[1], 'g-.', label='Point 1')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[2], 'b-', label='Point 2')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[3], 'k-', label='point 3')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[4], 'm--', label='point 4')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in -z direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fz_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_1_2_3_4.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

########################## yarn_position_5_6_7_8

plt.figure()
plt.plot(x_cord_2/(interval-2), 10**7*f_x[5], 'g-.', label='Point 5')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[6], 'b-', label='Point 6')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[7], 'k-', label='point 7')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[8], 'm--', label='point 8')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in x direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fx_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_5_6_7_8.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

plt.figure()
plt.plot(x_cord_2/(interval-2), 10**7*f_y[5], 'g-.', label='Point 5')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[6], 'b-', label='Point 6')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[7], 'k-', label='point 7')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[8], 'm--', label='point 8')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in y direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fy_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_5_6_7_8.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

plt.figure()
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[5], 'g-.', label='Point 5')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[6], 'b-', label='Point 6')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[7], 'k-', label='point 7')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[8], 'm--', label='point 8')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in -z direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fz_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_5_6_7_8.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()
############

########################## yarn_position_9_10_11_12

plt.figure()
plt.plot(x_cord_2/(interval-2), 10**7*f_x[9], 'g-.', label='Point 9')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[10], 'b-', label='Point 10')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[11], 'k-', label='point 11')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[12], 'm--', label='point 12')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in x direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fx_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_9_10_11_12.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

plt.figure()
plt.plot(x_cord_2/(interval-2), 10**7*f_y[9], 'g-.', label='Point 9')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[10], 'b-', label='Point 10')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[11], 'k-', label='point 11')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[12], 'm--', label='point 12')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in y direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fy_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_9_10_11_12.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

plt.figure()
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[9], 'g-.', label='Point 9')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[10], 'b-', label='Point 10')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[11], 'k-', label='point 11')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[12], 'm--', label='point 12')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in -z direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fz_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_9_10_11_12.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

########################## yarn_position_13_14_15

plt.figure()
plt.plot(x_cord_2/(interval-2), 10**7*f_x[13], 'g-.', label='Point 13')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[14], 'b-', label='Point 14')
plt.plot(x_cord_2/(interval-2), 10**7*f_x[15], 'k-', label='point 15')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in x direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fx_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_13_14_15.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

plt.figure()
plt.plot(x_cord_2/(interval-2), 10**7*f_y[13], 'g-.', label='Point 13')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[14], 'b-', label='Point 14')
plt.plot(x_cord_2/(interval-2), 10**7*f_y[15], 'k-', label='point 15')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in y direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fy_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_13_14_15.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

plt.figure()
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[13], 'g-.', label='Point 13')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[14], 'b-', label='Point 14')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z[15], 'k-', label='point 15')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')
plt.title('Force in -z direction along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Fz_distribution_setup_" + str(i) + "_yarn_speed_" + str(speed) +"_yarn_position_13_14_15.png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()
############