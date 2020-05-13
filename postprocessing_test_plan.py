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
i=24
point = input("the location of the yarn is: ")
# point = 1
speed = 90

#### speed = input("the speed of the yarn is: ")

reed_type = eval("setup_"+str(i)+".reed")
interval = eval("setup_"+str(i)+".interval")
y_n = eval("setup_"+str(i)+".y_n")
z_n= eval("setup_"+str(i)+".z_n")
alpha= eval("setup_" + str(i) + ".alpha")
beta= eval("setup_" + str(i) + ".beta")
diameter= eval("setup_" + str(i) + ".n_diameter")
p_in = eval("setup_" + str(i) + ".p_in")


######## set the directory

journal_setup_dir = "/cfdfile2/data/fm/alireza/EcoFlow/Test_plan/setup_"+str(i)+"/setup_"+str(i)+"_yarn_position_"+str(point)+"" \
                                    "/setup_"+str(i)+"_yarn_position_"+str(point)+"_yarn_speed_"+str(speed)+""
os.chdir(journal_setup_dir)
direct= os.getcwd()

#### cppy cunstom field function to the directory:

custom_dir_momentum = "/cfdfile2/data/fm/alireza/EcoFlow/reed_channel/simulation/momen-definition.scm"
copy_custom_momentum = "cp "+custom_dir_momentum+" "+journal_setup_dir+""
os.system(copy_custom_momentum)

custom_dir_mass_density = "/cfdfile2/data/fm/alireza/EcoFlow/reed_channel/simulation/density*vz.scm"
copy_custom_mass_density = "cp "+custom_dir_mass_density+" "+journal_setup_dir+""
os.system(copy_custom_mass_density)


####### define the journal file

fluent_file_name = "setup_"+str(i)+"_position_"+str(point)+"_speed_"+str(speed)+""

journal_postprocessing_name= "journal_postprocessing_setup_"+str(i)+"_position_"+str(point)+"_speed_"+str(speed)+".jou"


file_postprocessing = open(journal_postprocessing_name, "w")
file_postprocessing.write("file read-case-data "+fluent_file_name+".cas \n")

############### velocity vector at x-planes #########################

# thickness of the reed is:
reed_t = eval("setup_"+str(i)+".reed_thickness()")

# interval of the x-planes:
if reed_type == 2:
    x_interval=4.713872
elif reed_type == 3:
    x_interval = 4.6189
else:
    x_interval = 4.713379

# number of x-planes:
x_plane_int = floor((interval-reed_t-0.05)/x_interval)+1
print (x_plane_int)

counter_x = x_plane_int
counter_x_int = int(counter_x)

line_x_1 = [None] *20
line_x_2 = [None] *20
line_x_3 = [None] *20
line_x_4 = [None] *20
line_x_5 = [None] *20
line_x_6 = [None] *20
line_x_7 = [None] *20
line_x_8 = [None] *20
line_x_9 = [None] *20
line_x_10 = [None] *20
# image = [None] *20
matlab_m_vx = [None] *40
matlab_m_cy = [None] *40
matlab_m_cz = [None] *40
matlab_m_vy = [None] *40
matlab_m_vz = [None] *40
matlab_vx_1 = [None] *40
matlab_vx_2 = [None] *40
matlab_vy_1 = [None] *40
matlab_vy_2 = [None] *40
matlab_vz_1 = [None] *40
matlab_vz_2 = [None] *40
matlab_cy_1 = [None] *40
matlab_cy_2 = [None] *40
matlab_cz_1 = [None] *40
matlab_cz_2 = [None] *40


#for i in range(1, x_plane_int+1):
#for i in range(1, 17):


for j in range(0, counter_x_int):

    xx= (reed_t+0.05+x_interval*j)/1000
    x= (reed_t+0.05+x_interval*j)

    line_x_1[j] = "surface iso-surface x-coordinate x-"+str(x)+" () () "+str(xx)+" () \n"
    line_x_2[j] = "display set velocity-vectors auto-scale yes global-range no scale 40 in-plane yes scale-head 0.4 " \
                  "component-x no surfaces x-"+str(x)+" () \n"
    line_x_3[j] = "display vector velocity velocity-magnitude 0 300 80 1 \n"
    line_x_4[j] = "display views restore-view right \n"
    line_x_5[j] = "display views auto-scale \n"
    line_x_6[j] = "display views camera zoom-camera 5 \n"
    line_x_7[j] = "display views camera target "+str(xx)+" -0.004 0.007 \n"
    line_x_8[j] = "display set picture driver png \n"
    line_x_9[j] = "display save-picture \"vector_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_" \
                    "speed_" + str(speed)+"_x_"+str(x)+".png\" \n"
    line_x_10[j] = "file export ascii velocity_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + "_x-"+str(x)+".csv x-"+str(x)+"() no x-velocity y-velocity z-velocity () yes \n"
    # image_vx[i] = "vector_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+"_x_"+str(x)+".png"

    file_postprocessing.write(line_x_1[j])
    file_postprocessing.write(line_x_2[j])
    file_postprocessing.write(line_x_3[j])
    file_postprocessing.write(line_x_4[j])
    file_postprocessing.write(line_x_5[j])
    file_postprocessing.write(line_x_6[j])
    file_postprocessing.write(line_x_7[j])
    file_postprocessing.write(line_x_8[j])
    file_postprocessing.write(line_x_9[j])
    file_postprocessing.write(line_x_10[j])

    matlab_vx_1[j] = "I_cx=imread(strcat('vector_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + "_x_" + str(x) + ".png'));\n"
    matlab_vx_2[j] = "writeVideo(video_vector_x_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_"+str(speed)+",I_cx); \n"

matlab_m_vx[0] = "video_vector_x_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+" =" \
            "VideoWriter('video_vector_x_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".avi'); \n"
matlab_m_vx[1] = "video_vector_x_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".FrameRate = 2; \n"
matlab_m_vx[2] = "video_vector_x_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".Quality = 75\n"
matlab_m_vx[3] = "open(video_vector_x_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+");\n"

# make video

make_video_mfile = open("make_video.m", "w")
make_video_mfile.write("clear all \n")
for index_1 in range(4):
    make_video_mfile.write(matlab_m_vx[index_1])
# for index_2 in range(16):
for index_2 in range(counter_x_int):
    make_video_mfile.write(matlab_vx_1[index_2])
    make_video_mfile.write(matlab_vx_2[index_2])
make_video_mfile.write("close(video_vector_x_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+"); \n")


############### velocity contour and vector at y-planes #########################
yy_1= [None] *20
yy_2= [None] *20
yy_3= [None] *20
yy_4= [None] *20
yy_5= [None] *20
yy_6= [None] *20
yy_7= [None] *20
yy_8= [None] *20
yy_9= [None] *20
yy_10= [None] *20

y= array.array('d', [0, -0.2, -0.5, -1, -1.5, -2, -2.5, -3, -3.5, -4, -4.5, -5, -5.5, -6])

for ii in range(len(y)):
    yy_1[ii] = "surface iso-surface y-coordinate y-"+str(y[ii])+" () () "+str(y[ii]/1000)+" () \n"
    yy_2[ii] = "display set lights headlight-on no \n"
    yy_3[ii] = "display set lights lights-on no \n"
    yy_4[ii] = "display set contours auto-range no global-range no coloring no filled-contours yes surfaces y-"+str(y[ii])+" () \n"
    yy_5[ii] = "display contour velocity-magnitude 0 250 \n"
    yy_6[ii] = "display views restore-view top \n"
    yy_7[ii] = "display views auto-scale \n"
    yy_8[ii] = "display views camera zoom-camera 0.75 \n"
    if interval == 40:
        yy_9[ii] = "display views camera target 0.03 "+str(y[ii]/1000)+" 0.0022 \n"
    else:
        yy_9[ii] = "display views camera target 0.05 "+str(y[ii]/1000)+" 0.0022 \n"
    yy_10[ii] = "display save-picture \"contour_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_" \
                                "speed_" + str(speed)+"_y_"+str(y[ii])+".png\" \n"

    file_postprocessing.write(yy_1[ii])
    file_postprocessing.write(yy_2[ii])
    file_postprocessing.write(yy_3[ii])
    file_postprocessing.write(yy_4[ii])
    file_postprocessing.write(yy_5[ii])
    file_postprocessing.write(yy_6[ii])
    file_postprocessing.write(yy_7[ii])
    file_postprocessing.write(yy_8[ii])
    file_postprocessing.write(yy_9[ii])
    file_postprocessing.write(yy_10[ii])

    matlab_cy_1[ii] = "I_cy=imread(strcat('contour_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + "_y_" + str(y[ii]) + ".png'));\n"
    matlab_cy_2[ii] = "writeVideo(video_contour_y_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + ",I_cy); \n"

matlab_m_cy[0] = "video_contour_y_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+" =" \
            "VideoWriter('video_contour_y_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".avi'); \n"
matlab_m_cy[1] = "video_contour_y_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".FrameRate = 2; \n"
matlab_m_cy[2] = "video_contour_y_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".Quality = 75\n"
matlab_m_cy[3] = "open(video_contour_y_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+");\n"

#video
for index_1 in range(4):
    make_video_mfile.write(matlab_m_cy[index_1])
for index_2 in range(len(y)):
    make_video_mfile.write(matlab_cy_1[index_2])
    make_video_mfile.write(matlab_cy_2[index_2])
make_video_mfile.write("close(video_contour_y_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+"); \n")
#

vy_1= [None] *20
vy_2= [None] *20
vy_3= [None] *20
vy_4= [None] *20
vy_5= [None] *20
vy_6= [None] *20
vy_7= [None] *20
vy_8= [None] *20
vy_9= [None] *20
vy_10= [None] *20

for ii in range(len(y)):
    vy_1[ii] = "display set lights headlight-on no \n"
    vy_2[ii] = "display set lights lights-on no \n"
    vy_3[ii] = "display set velocity-vectors auto-scale y global-range n scale 300 in-plane y scale-head 0.4 component" \
               "-x y velocity-magnitude component-y n component-z y velocity-magnitude surfaces y-"+str(y[ii])+" () \n"
    vy_4[ii] = "display vector velocity velocity-magnitude 0 250 400 150 \n"
    vy_5[ii] = "display views restore-view top \n"
    vy_6[ii] = "display views auto-scale \n"
    vy_7[ii] = "display views camera zoom-camera 0.9 \n"
    if interval == 40:
        vy_8[ii] = "display views camera target 0.025 "+str(y[ii]/1000)+" 0.0022 \n"
    else:
        vy_8[ii] = "display views camera target 0.045 "+str(y[ii]/1000)+" 0.0022 \n"

    vy_9[ii] = "display save-picture \"vector_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_" \
                    "speed_" + str(speed)+"_y_"+str(y[ii])+".png\" \n"
    vy_10[ii] = "file export ascii velocity_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + "_y-"+str(y[ii])+".csv y-"+str(y[ii])+" () no x-velocity y-velocity z-velocity () yes \n"

    file_postprocessing.write(vy_1[ii])
    file_postprocessing.write(vy_2[ii])
    file_postprocessing.write(vy_3[ii])
    file_postprocessing.write(vy_4[ii])
    file_postprocessing.write(vy_5[ii])
    file_postprocessing.write(vy_6[ii])
    file_postprocessing.write(vy_7[ii])
    file_postprocessing.write(vy_8[ii])
    file_postprocessing.write(vy_9[ii])
    file_postprocessing.write(vy_10[ii])

    matlab_vy_1[ii] = "I_vy=imread(strcat('vector_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + "_y_" + str(y[ii]) + ".png'));\n"
    matlab_vy_2[ii] = "writeVideo(video_vector_y_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + ",I_vy); \n"

matlab_m_vy[0] = "video_vector_y_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+" =" \
            "VideoWriter('video_vector_y_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".avi'); \n"
matlab_m_vy[1] = "video_vector_y_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".FrameRate = 2; \n"
matlab_m_vy[2] = "video_vector_y_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".Quality = 75\n"
matlab_m_vy[3] = "open(video_vector_y_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+");\n"

#video
for index_1 in range(4):
    make_video_mfile.write(matlab_m_vy[index_1])
for index_2 in range(len(y)):
    make_video_mfile.write(matlab_vy_1[index_2])
    make_video_mfile.write(matlab_vy_2[index_2])
make_video_mfile.write("close(video_vector_y_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+"); \n")
#

############### velocity contour and vector at z-planes #########################

zz_1= [None] *20
zz_2= [None] *20
zz_3= [None] *20
zz_4= [None] *20
zz_5= [None] *20
zz_6= [None] *20
zz_7= [None] *20
zz_8= [None] *20
zz_9= [None] *20
zz_10= [None] *20

z= array.array('d', [0, 0.2, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])

for ii in range(len(z)):
    zz_1[ii] = "surface iso-surface z-coordinate z-"+str(z[ii])+" () () "+str(z[ii]/1000)+" () \n"
    zz_2[ii] = "display set lights headlight-on no \n"
    zz_3[ii] = "display set lights lights-on no \n"
    zz_4[ii] = "display set contours auto-range no global-range no coloring no filled-contours yes surfaces z-"+str(z[ii])+" () \n"
    zz_5[ii] = "display contour velocity-magnitude 0 250 \n"
    zz_6[ii] = "display views restore-view front \n"
    zz_7[ii] = "display views auto-scale \n"
    zz_8[ii] = "display views camera zoom-camera 0.75 \n"
    zz_9[ii] = "display views camera target 0.025 -0.0023 "+str(z[ii]/1000)+"\n"
    zz_10[ii] = "display save-picture \"contour_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_" \
                                "speed_" + str(speed)+"_z_"+str(z[ii])+".png\" \n"

    file_postprocessing.write(zz_1[ii])
    file_postprocessing.write(zz_2[ii])
    file_postprocessing.write(zz_3[ii])
    file_postprocessing.write(zz_4[ii])
    file_postprocessing.write(zz_5[ii])
    file_postprocessing.write(zz_6[ii])
    file_postprocessing.write(zz_7[ii])
    file_postprocessing.write(zz_8[ii])
    file_postprocessing.write(zz_9[ii])
    file_postprocessing.write(zz_10[ii])

    matlab_cz_1[ii] = "I_cz=imread(strcat('contour_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + "_z_" + str(z[ii]) + ".png'));\n"
    matlab_cz_2[ii] = "writeVideo(video_contour_z_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + ",I_cz); \n"

matlab_m_cz[0] = "video_contour_z_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+" =" \
            "VideoWriter('video_contour_z_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".avi'); \n"
matlab_m_cz[1] = "video_contour_z_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".FrameRate = 2; \n"
matlab_m_cz[2] = "video_contour_z_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".Quality = 75\n"
matlab_m_cz[3] = "open(video_contour_z_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+");\n"

#video
for index_1 in range(4):
    make_video_mfile.write(matlab_m_cz[index_1])
for index_2 in range(len(z)):
    make_video_mfile.write(matlab_cz_1[index_2])
    make_video_mfile.write(matlab_cz_2[index_2])
make_video_mfile.write("close(video_contour_z_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+"); \n")
#

vz_1= [None] *20
vz_2= [None] *20
vz_3= [None] *20
vz_4= [None] *20
vz_5= [None] *20
vz_6= [None] *20
vz_7= [None] *20
vz_8= [None] *20
vz_9= [None] *20
vz_10= [None] *20

for ii in range(len(z)):
    vz_1[ii] = "display set lights headlight-on no \n"
    vz_2[ii] = "display set lights lights-on no \n"
    vz_3[ii] = "display set velocity-vectors auto-scale y global-range n scale 200 in-plane y scale-head 0.4 component" \
               "-x y velocity-magnitude component-y y velocity-magnitude component-z n surfaces z-"+str(z[ii])+" () \n"
    vz_4[ii] = "display vector velocity velocity-magnitude 0 250 100 50 \n"
    vz_5[ii] = "display views restore-view front \n"
    vz_6[ii] = "display views auto-scale \n"
    vz_7[ii] = "display views camera zoom-camera 2.5 \n"
    if interval == 40:
        vz_8[ii] = "display views camera target 0.02 -0.0035 "+str(z[ii]/1000)+" \n"
    else:
        vz_8[ii] = "display views camera target 0.04 -0.0035 "+str(z[ii]/1000)+" \n"
    vz_9[ii] = "display save-picture \"vector_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_" \
                    "speed_" + str(speed)+"_z_"+str(z[ii])+".png\" \n"
    vz_10[ii] = "file export ascii velocity_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + "_z-"+str(z[ii])+".csv z-"+str(z[ii])+" () no x-velocity y-velocity z-velocity () yes \n"

    file_postprocessing.write(vz_1[ii])
    file_postprocessing.write(vz_2[ii])
    file_postprocessing.write(vz_3[ii])
    file_postprocessing.write(vz_3[ii])
    file_postprocessing.write(vz_4[ii])
    file_postprocessing.write(vz_5[ii])
    file_postprocessing.write(vz_6[ii])
    file_postprocessing.write(vz_7[ii])
    file_postprocessing.write(vz_8[ii])
    file_postprocessing.write(vz_9[ii])
    file_postprocessing.write(vz_10[ii])

    matlab_vz_1[ii] = "I_vz=imread(strcat('vector_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + "_z_" + str(z[ii]) + ".png'));\n"
    matlab_vz_2[ii] = "writeVideo(video_vector_z_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + ",I_vz); \n"

matlab_m_vz[0] = "video_vector_z_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+" =" \
            "VideoWriter('video_vector_z_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".avi'); \n"
matlab_m_vz[1] = "video_vector_z_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".FrameRate = 2; \n"
matlab_m_vz[2] = "video_vector_z_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".Quality = 75\n"
matlab_m_vz[3] = "open(video_vector_z_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+");\n"

#video
for index_1 in range(4):
    make_video_mfile.write(matlab_m_vz[index_1])
for index_2 in range(len(z)):
    make_video_mfile.write(matlab_vz_1[index_2])
    make_video_mfile.write(matlab_vz_2[index_2])
make_video_mfile.write("close(video_vector_z_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+"); \n")

make_video_mfile.write("quit \n")
make_video_mfile.close()

############### velocity and total pressure profile across the reed channel #########################

line_surface_1 = "surface line-surface y=-2.8_z=1 0 -0.0028 0.001 "+str(interval/1000)+" -0.0028 0.001 \n"
line_surface_2 = "surface line-surface y=-2.8_z=3 0 -0.0028 0.003 "+str(interval/1000)+" -0.0028 0.003 \n"
line_surface_3 = "surface line-surface y=-2.8_z=5 0 -0.0028 0.005 "+str(interval/1000)+" -0.0028 0.005 \n"

plot_v_1 = "plot plot yes \"veocity-y=-2.8-z=1_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".txt\" no no no velocity-magnitude yes 1 0 0 y=-2.8_z=1 () \n"
plot_v_2 = "plot plot yes \"veocity-y=-2.8-z=3_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".txt\" no no no velocity-magnitude yes 1 0 0 y=-2.8_z=3 () \n"
plot_v_3 = "plot plot yes \"veocity-y=-2.8-z=5_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".txt\" no no no velocity-magnitude yes 1 0 0 y=-2.8_z=5 () \n"
plot_p_1 = "plot plot yes \"total-pressure-y=-2.8-z=1_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".txt\" no no no total-pressure yes 1 0 0 y=-2.8_z=1 () \n"
plot_p_2 = "plot plot yes \"total-pressure-y=-2.8-z=3_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".txt\" no no no total-pressure yes 1 0 0 y=-2.8_z=3 () \n"
plot_p_3 = "plot plot yes \"total-pressure-y=-2.8-z=5_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".txt\" no no no total-pressure yes 1 0 0 y=-2.8_z=5 () \n"

file_postprocessing.write(line_surface_1)
file_postprocessing.write(line_surface_2)
file_postprocessing.write(line_surface_3)
file_postprocessing.write(plot_v_1)
file_postprocessing.write(plot_v_2)
file_postprocessing.write(plot_v_3)
file_postprocessing.write(plot_p_1)
file_postprocessing.write(plot_p_2)
file_postprocessing.write(plot_p_3)

############### mass flow rate and momentum across the reed channel #########################

clip= [None] *15
surface_xx = [None] *15
clip_y_x = [None] *15
clip_zy_x= [None] *15
x_name = [None] *15

for kk in range(15):
    clip[kk]= 0.005*kk

    surface_xx[kk] ="surface iso-surface x-coordinate x-"+str(clip[kk])+" () () "+str(clip[kk])+" () \n"
    clip_y_x[kk] = "surface iso-clip y-coordinate clip-y-x-"+str(clip[kk])+" x-"+str(clip[kk])+" -0.00675 0 \n"
    clip_zy_x[kk] = "surface iso-clip z-coordinate clip-zy-x-"+str(clip[kk])+" clip-y-x-"+str(clip[kk])+" 0 0.005 \n"
    x_name[kk] ="clip-zy-x-"+str(clip[kk])+" "

    file_postprocessing.write(surface_xx[kk])
    file_postprocessing.write(clip_y_x[kk])
    file_postprocessing.write(clip_zy_x[kk])

all_name = "".join(x_name[0:15])
clip_mass = "report surface-integrals mass-flow-rate "+all_name+" () yes \"mass-flow-clip-yz_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".txt\" \n"
clip_momentum = "report surface-integrals integral "+all_name+" () momen yes \"momentum-flow-clip-yz_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".txt\" \n"
momen_define ="define custom-field-functions load \"momen-definition.scm\" \n"

file_postprocessing.write(clip_mass)
file_postprocessing.write(momen_define)
file_postprocessing.write(clip_momentum)

###############% contour density*vz ###############

define_zz_1 = "define custom-field-functions load \"density*vz.scm\" \n"
surface_zz_1 = "surface iso-surface z-coordinate z--5 () () -0.005 () \n"
contour_zz_1 = "display set contours auto-range no global-range no coloring no filled-contours yes surfaces z--5 () \n"
range_zz_1 ="display contour density_x_vz 0 50 \n"
disp_zz_1 = "display views restore-view front \n"
save_fig_zz_1 = "display save-picture \"countour_density_x_Vz_setup"+ str(i)+"_yarn_position_" + str(point)+"_yarn_" \
                                    "speed_" + str(speed)+"_z_-5.png\" \n"

contour_zz_2 = "display set contours auto-range no global-range no coloring no filled-contours yes surfaces z-5.0 () \n"
range_zz_2 ="display contour density_x_vz 0 70 \n"
disp_zz_2 = "display views restore-view front \n"
save_fig_zz_2 = "display save-picture \"countour_density_x_Vz_setup"+ str(i)+"_yarn_position_" + str(point)+"_yarn_" \
                                    "speed_" + str(speed)+"_z_5.png\" \n"

file_postprocessing.write(define_zz_1)
file_postprocessing.write(surface_zz_1)
file_postprocessing.write(contour_zz_1)
file_postprocessing.write(range_zz_1)
file_postprocessing.write(disp_zz_1)
file_postprocessing.write(save_fig_zz_1)
file_postprocessing.write(contour_zz_2)
file_postprocessing.write(range_zz_2)
file_postprocessing.write(disp_zz_2)
file_postprocessing.write(save_fig_zz_2)

############### UDF for force along the yarn ###############

main_journal_setup_dir = "/cfdfile2/data/fm/alireza/EcoFlow/reed_channel/simulation"
os.chdir(main_journal_setup_dir)
main_direct= os.getcwd()

file_j_1=open("Get_all_Forces.c", "r")
file_j_1_lines = file_j_1.readlines()

if interval == 60 and reed_type == "Reed_1" or diameter == 1.3:
    file_j_1_lines[1] = "#define WALLID 27 /* Take care that you list the correct value here */ \n"

file_j_1_lines[2] = "#define F_NAME \"Force_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_" \
                    "speed_" + str(speed)+".txt\" \n"

udf_dir = "/cfdfile2/data/fm/alireza/EcoFlow/Test_plan/setup_"+str(i)+"/setup_"+str(i)+"_yarn_position_"+str(point)+"" \
                                    "/setup_"+str(i)+"_yarn_position_"+str(point)+"_yarn_speed_"+str(speed)+""
os.chdir(udf_dir)
direct= os.getcwd()
filename_udf = "Get_all_forces_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_" + str(speed)+".c"
file_udf=open(filename_udf, "w")
for l in file_j_1_lines:
    file_udf.write(l)
file_udf.close()


file_postprocessing.write("define user-defined compiled-functions compile libudf yes "+filename_udf+" \"\" \"\" \n \n")
file_postprocessing.write("define user-defined compiled-functions load libudf \n \n")
file_postprocessing.write("define user-defined execute-on-demand \"store_data::libudf\" \n")
file_postprocessing.write("exit yes \n")
file_postprocessing.close()

######## read and run the created journal file ##############

fluent_command = "fluent 3ddp -i "+journal_postprocessing_name+" -t36"
os.system(fluent_command)
#

######## Force distribution on the yarn ##############

# os.chdir(udf_dir)

### modify the file
file_2=open("Force_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_" + str(speed)+".txt", "r")
file_2_lines = file_2.readlines()
range_file_2 = len(file_2_lines)

force_filename = "Force_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + ".csv"

file_force_1 = open(force_filename, "w")
for a in range(1, len(file_2_lines)):
     file_force_1.write(file_2_lines[a])
file_force_1.close()
#####

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

for j in range(0,ring_elment):
    x_cord[j] = (sort_1[j][0]-0.00105)*1000
    p_f_x[j] = sort_1[j][3]
    p_f_y[j] = sort_1[j][4]
    p_f_z[j] = sort_1[j][5]
    v_f_x[j] = sort_1[j][6]
    v_f_y[j] = sort_1[j][7]
    v_f_z[j] = sort_1[j][8]

x_cord_2 = np.zeros(ring_elment/40)
pressure_force_x = np.zeros(ring_elment/40)
pressure_force_y = np.zeros(ring_elment/40)
pressure_force_z = np.zeros(ring_elment/40)
viscous_force_x = np.zeros(ring_elment/40)
viscous_force_y = np.zeros(ring_elment/40)
viscous_force_z = np.zeros(ring_elment/40)

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

f_x = pressure_force_x+viscous_force_x
f_y = pressure_force_y+viscous_force_y
f_z = pressure_force_z+viscous_force_z
f_0 = np.zeros(ring_elment/40)

total_force_x = sum(f_x)
total_pressure_force_x = sum(pressure_force_x)
total_viscous_force_x = sum(viscous_force_x)

total_force_y = sum(f_y)
total_pressure_force_y = sum(pressure_force_y)
total_viscous_force_y = sum(viscous_force_y)

total_force_z = sum(f_z)
total_pressure_force_z = sum(pressure_force_z)
total_viscous_force_z = sum(viscous_force_z)

### net forces on the yarn ###
net_force_per_lenght = open("net_force_setup_"+ str(i)+"_yarn_position_"+str(point)+"_yarn_speed_"+str(speed)+".txt","w")
net_force_per_lenght.write("Forces (mN/m) components: Fx/L  Fy/L    Fz/L \n")
net_force_per_lenght.write("Viscous Forces per yarn lenght:"+str(10**6*total_viscous_force_x/(interval-2))+
                           "   "+str(10**6*total_viscous_force_y/(interval-2)) +"  "+str(10**6*total_viscous_force_z/(interval-2))+" \n")
net_force_per_lenght.write("Pressure Forces per yarn lenght:"+str(10**6*total_pressure_force_x/(interval-2)) +
                            "   "+str(10**6*total_pressure_force_y/(interval-2)) +"  "+str(10**6*total_pressure_force_z/(interval-2))+" \n")
net_force_per_lenght.write("Net Forces per yarn lenght:"+str(10**6*total_force_x/(interval-2)) +
                            "   "+str(10**6*total_force_y/(interval-2)) +"  "+str(10**6*total_force_z/(interval-2))+" \n")
net_force_per_lenght.close()

###############################

### forces distribution along the yarn ###

## force components

plt.figure()
plt.plot(x_cord_2/(interval-2), 10**7*f_x, 'g-.', label='Fx')
plt.plot(x_cord_2/(interval-2), 10**7*f_y, 'b-', label='Fy')
plt.plot(x_cord_2/(interval-2), -1*10**7*f_z, 'k-', label='-Fz')
plt.plot(x_cord_2/(interval-2), f_0 ,'r-.', label='F=0')

plt.title('Force along the yarn')
plt.xlabel('x/L')
plt.ylabel('Force/(0.1mm) (mN/m)')
plt.legend(loc='best')
pic_name= "Force_distribution_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) +".png"
plt.savefig(pic_name, transparent=False)
#plt.show()
plt.close()
############

if point == 2 or point == 3 or point == 4:
    plt.figure()
    plt.plot(x_cord_2/(interval-2), 10 ** 7 * (f_x-0.1*f_y), 'g-.', label='$\mu=0.1$')
    plt.plot(x_cord_2/(interval-2), 10 ** 7 * (f_x-0.15*f_y), 'b-', label='$\mu=0.15$')
    plt.plot(x_cord_2/(interval-2), 10 ** 7 * (f_x-0.2*f_y), 'k-', label='$\mu=0.2$')
    plt.plot(x_cord_2/(interval-2), 10 ** 7 * (f_x-0.25*f_y), 'r-.', label='$\mu=0.25$')
    plt.plot(x_cord_2/(interval-2), 10 ** 7 * (f_x-0.3*f_y), 'c-', label='$\mu=0.3$')
    plt.plot(x_cord_2 / (interval - 2), f_0, 'y-.', label='F=0')

    plt.title('$Fx-\mu Fy$')
    plt.xlabel('x/L')
    plt.ylabel('Fx/(0.1mm) (mN/m)')
    plt.legend(loc='best')
    pic_name = "Force_x_friction_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(
        speed) + ".png"
    plt.savefig(pic_name, transparent=False)
    # plt.show()
    plt.close()

elif point == 5 or point == 9:
    plt.figure()
    plt.plot(x_cord_2 / (interval - 2), 10 ** 7 * (f_x - 0.1 * np.absolute(f_z)), 'g-.', label='$\mu=0.1$')
    plt.plot(x_cord_2 / (interval - 2), 10 ** 7 * (f_x - 0.15 * np.absolute(f_z)), 'b-', label='$\mu=0.15$')
    plt.plot(x_cord_2 / (interval - 2), 10 ** 7 * (f_x - 0.2 * np.absolute(f_z)), 'k-', label='$\mu=0.2$')
    plt.plot(x_cord_2 / (interval - 2), 10 ** 7 * (f_x - 0.25 * np.absolute(f_z)), 'r-.', label='$\mu=0.25$')
    plt.plot(x_cord_2 / (interval - 2), 10 ** 7 * (f_x - 0.3 * np.absolute(f_z)), 'c-', label='$\mu=0.3$')
    plt.plot(x_cord_2 / (interval - 2), f_0, 'y-.', label='F=0')

    plt.title('$Fx-\mu Fz$')
    plt.xlabel('x/L')
    plt.ylabel('Fx/(0.1mm) (mN/m)')
    plt.legend(loc='best')
    pic_name = "Force_x_friction_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(
        speed) + ".png"
    plt.savefig(pic_name, transparent=False)
    # plt.show()
    plt.close()

elif point == 1:
    plt.figure()
    plt.plot(x_cord_2 / (interval - 2), 10 ** 7 * (f_x - 0.1 * np.sqrt(f_z**2+f_y**2)), 'g-.', label='$\mu=0.1$')
    plt.plot(x_cord_2 / (interval - 2), 10 ** 7 * (f_x - 0.15 * np.sqrt(f_z**2+f_y**2)), 'b-', label='$\mu=0.15$')
    plt.plot(x_cord_2 / (interval - 2), 10 ** 7 * (f_x - 0.2 * np.sqrt(f_z**2+f_y**2)), 'k-', label='$\mu=0.2$')
    plt.plot(x_cord_2 / (interval - 2), 10 ** 7 * (f_x - 0.25 * np.sqrt(f_z**2+f_y**2)), 'r-.', label='$\mu=0.25$')
    plt.plot(x_cord_2 / (interval - 2), 10 ** 7 * (f_x - 0.3 * np.sqrt(f_z**2+f_y**2)), 'c-', label='$\mu=0.3$')
    plt.plot(x_cord_2 / (interval - 2), f_0, 'y-.', label='F=0')

    plt.title('$Fx-\mu (Fz^{2}+Fy^{2})^{0.5}$')
    plt.xlabel('x/L')
    plt.ylabel('Fx/(0.1mm) (mN/m)')
    plt.legend(loc='best')
    pic_name = "Force_x_friction_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(
        speed) + ".png"
    plt.savefig(pic_name, transparent=False)
    # plt.show()
    plt.close()

########### velocity and total pressure profiles #####
### modify files

### z =1
file_v_1=open("veocity-y=-2.8-z=1_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".txt", "r")
file_v_1_lines = file_v_1.readlines()
v_1_filename = "veocity-y=-2.8-z=1_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + ".csv"
v_1 = open(v_1_filename, "w")
for aa in range(4, len(file_v_1_lines)-1):
     v_1.write(file_v_1_lines[aa])
v_1.close()

list_v_1 = [None] *(len(file_v_1_lines)-5)
with open(v_1_filename, "r") as f:
     lst_v_1 = [float(line_v1) for line_v1 in f.read().split()]

for jj in range(0,len(file_v_1_lines)-5,1):
     list_v_1[jj] = lst_v_1[0 + 2 * jj : 2 + 2 * jj]

sort_v_1 = sorted(list_v_1, key=operator.itemgetter(0))
x_v_1 = np.zeros(len(file_v_1_lines)-5)
vel_1=np.zeros(len(file_v_1_lines)-5)

for j in range(0,len(file_v_1_lines)-5):
    x_v_1[j] = (sort_v_1[j][0])*1000
    vel_1[j] = sort_v_1[j][1]

### z =3
file_v_3=open("veocity-y=-2.8-z=3_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".txt", "r")
file_v_3_lines = file_v_3.readlines()
v_3_filename = "veocity-y=-2.8-z=3_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + ".csv"
v_3 = open(v_3_filename, "w")
for aa in range(4, len(file_v_3_lines)-1):
     v_3.write(file_v_3_lines[aa])
v_3.close()

list_v_3 = [None] *(len(file_v_3_lines)-5)

with open(v_3_filename, "r") as f:
     lst_v_3 = [float(line_v3) for line_v3 in f.read().split()]

for jj in range(0,len(file_v_3_lines)-5,1):
     list_v_3[jj] = lst_v_3[0 + 2 * jj : 2 + 2 * jj]

sort_v_3 = sorted(list_v_3, key=operator.itemgetter(0))
x_v_3 = np.zeros(len(file_v_3_lines)-5)
vel_3=np.zeros(len(file_v_3_lines)-5)

for j in range(0,len(file_v_3_lines)-5):
    x_v_3[j] = (sort_v_3[j][0])*1000
    vel_3[j] = sort_v_3[j][1]

### z =5

file_v_5=open("veocity-y=-2.8-z=5_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".txt", "r")
file_v_5_lines = file_v_5.readlines()
v_5_filename = "veocity-y=-2.8-z=5_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + ".csv"
v_5 = open(v_5_filename, "w")
for aa in range(4, len(file_v_5_lines)-1):
     v_5.write(file_v_5_lines[aa])
v_5.close()

list_v_5 = [None] *(len(file_v_5_lines)-5)
with open(v_5_filename, "r") as f:
     lst_v_5 = [float(line_v5) for line_v5 in f.read().split()]
for jj in range(0,len(file_v_5_lines)-5,1):
     list_v_5[jj] = lst_v_5[0 + 2 * jj : 2 + 2 * jj]
sort_v_5 = sorted(list_v_5, key=operator.itemgetter(0))
x_v_5 = np.zeros(len(file_v_5_lines)-5)
vel_5=np.zeros(len(file_v_5_lines)-5)

for j in range(0,len(file_v_5_lines)-5):
    x_v_5[j] = (sort_v_5[j][0])*1000
    vel_5[j] = sort_v_5[j][1]

##  plot the velocity profiles

plt.figure()
plt.plot(x_v_1, vel_1, 'g-.', label='y=-2.8mm & z=1mm')
plt.plot(x_v_3, vel_3, 'b-', label='y=-2.8mm & z=3mm')
plt.plot(x_v_5, vel_5, 'k-', label='y=-2.8mm & z=5mm')
plt.title('velocity profiles')
plt.xlabel('x(mm)')
plt.ylabel('Velocity (m/s)')
plt.legend(loc='best')
pic_name= "velocity_reed_channel_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) +".png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()

####################
### modify pressure files files

file_p_1=open("total-pressure-y=-2.8-z=1_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".txt", "r")
file_p_1_lines = file_p_1.readlines()
p_1_filename = "total-pressure-y=-2.8-z=1_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + ".csv"
p_1 = open(p_1_filename, "w")
for aa in range(4, len(file_p_1_lines)-1):
     p_1.write(file_p_1_lines[aa])
p_1.close()

list_p_1 = [None] *(len(file_p_1_lines)-5)
with open(p_1_filename, "r") as f:
     lst_p_1 = [float(line_p1) for line_p1 in f.read().split()]

for jj in range(0,len(file_p_1_lines)-5,1):
     list_p_1[jj] = lst_p_1[0 + 2 * jj : 2 + 2 * jj]

sort_p_1 = sorted(list_p_1, key=operator.itemgetter(0))
x_p_1 = np.zeros(len(file_p_1_lines)-5)
pres_1=np.zeros(len(file_p_1_lines)-5)

for j in range(0,len(file_p_1_lines)-5):
    x_p_1[j] = (sort_p_1[j][0])*1000
    pres_1[j] = sort_p_1[j][1]

####
file_p_3=open("total-pressure-y=-2.8-z=3_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".txt", "r")
file_p_3_lines = file_p_3.readlines()
p_3_filename = "total-pressure-y=-2.8-z=3_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + ".csv"
p_3 = open(p_3_filename, "w")
for aa in range(4, len(file_p_3_lines)-1):
     p_3.write(file_p_3_lines[aa])
p_3.close()

list_p_3 = [None] *(len(file_p_3_lines)-5)
with open(p_3_filename, "r") as f:
     lst_p_3 = [float(line_p3) for line_p3 in f.read().split()]

for jj in range(0,len(file_p_3_lines)-5,1):
     list_p_3[jj] = lst_p_3[0 + 2 * jj : 2 + 2 * jj]

sort_p_3 = sorted(list_p_3, key=operator.itemgetter(0))
x_p_3 = np.zeros(len(file_p_3_lines)-5)
pres_3=np.zeros(len(file_p_3_lines)-5)

for j in range(0,len(file_p_3_lines)-5):
    x_p_3[j] = (sort_p_3[j][0])*1000
    pres_3[j] = sort_p_3[j][1]

####
file_p_5=open("total-pressure-y=-2.8-z=5_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".txt", "r")
file_p_5_lines = file_p_5.readlines()
p_5_filename = "total-pressure-y=-2.8-z=5_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) + ".csv"
p_5 = open(p_5_filename, "w")
for aa in range(4, len(file_p_5_lines)-1):
     p_5.write(file_p_5_lines[aa])
p_5.close()

list_p_5 = [None] *(len(file_p_5_lines)-5)

with open(p_5_filename, "r") as f:
     lst_p_5 = [float(line_p5) for line_p5 in f.read().split()]

for jj in range(0,len(file_p_5_lines)-5,1):
     list_p_5[jj] = lst_p_5[0 + 2 * jj : 2 + 2 * jj]

sort_p_5 = sorted(list_p_5, key=operator.itemgetter(0))
x_p_5 = np.zeros(len(file_p_5_lines)-5)
pres_5=np.zeros(len(file_p_5_lines)-5)

for j in range(0,len(file_p_5_lines)-5):
    x_p_5[j] = (sort_p_5[j][0])*1000
    pres_5[j] = sort_p_5[j][1]
###########
##  plot the total pressure profiles

plt.figure()
plt.plot(x_p_1, pres_1/100, 'g-.', label='y=-2.8mm & z=1mm')
plt.plot(x_p_3, pres_3/100, 'b-', label='y=-2.8mm & z=3mm')
plt.plot(x_p_5, pres_5/100, 'k-', label='y=-2.8mm & z=5mm')
plt.title('Total pressure profiles')
plt.xlabel('x(mm)')
plt.ylabel('Total pressure (mbar)')
plt.legend(loc='best')
pic_name= "Total_pressure_reed_channel_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) +".png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()
#############
######## mass and momentum along the channel ###
#
file_mass = open("mass-flow-clip-yz_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".txt", "r")
mass_lines = file_mass.readlines()

mass_m = [None]*(len(mass_lines)-6)
mass = np.zeros(len(mass_lines)-6)

for mm in range(4,len(mass_lines)-2,1):
    mass_m[mm-4]= mass_lines[mm].split()
    mass[mm-4] = mass_m[mm-4][1]
file_mass.close()
x_mass = 1000*np.asarray(clip[0:len(mass_lines)-6])
mass_flow = 3600/1.2929*mass

## plot mass flow rate
plt.figure()
plt.plot(x_mass, mass_flow, 'bo', label='mass flow rate')
plt.title('Mass flow rate along the reed channel')
plt.xlabel('x(mm)')
plt.ylabel('Mass flow rate $(Nm^{3}/h)$')
# plt.legend(loc='best')
pic_name= "Mass_flowrate_reed_channel_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) +".png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()


file_moment = open("momentum-flow-clip-yz_setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_"+ str(speed)+".txt", "r")
moment_lines = file_moment.readlines()
moment_m = [None]*(len(moment_lines)-7)
moment = np.zeros(len(moment_lines)-7)

for mm in range(5,len(moment_lines)-2):
    moment_m[mm-5]= moment_lines[mm].split()
    moment[mm-5] = moment_m[mm-5][1]
file_moment.close()
x_moment = 1000*np.asarray(clip[0:len(moment_lines)-7])

## plot momentum

plt.figure()
plt.plot(x_moment, moment, 'ko', label='momentum')
plt.title('Momentum along the reed channel')
plt.xlabel('x(mm)')
plt.ylabel('Momentum (N)')
# plt.legend(loc='best')
pic_name= "Momentum_reed_channel_setup_" + str(i) + "_yarn_position_" + str(point) + "_yarn_speed_" + str(speed) +".png"
plt.savefig(pic_name, transparent=False)
# plt.show()
plt.close()
##############
### call matlab for creading video

command_matlab = "matlab -nosplash -nodesktop < make_video.m"
os.system(command_matlab)

### remove redundant files


command_remove_1 ="rm *.scm"
command_remove_2 ="rm *.jou"
command_remove_3 ="rm *.c"
command_remove_4 ="rm "+force_filename+""
command_remove_5 ="rm "+v_1_filename+""
command_remove_6 ="rm "+v_3_filename+""
command_remove_7 ="rm "+v_5_filename+""
command_remove_8 ="rm "+p_1_filename+""
command_remove_9 ="rm "+p_3_filename+""
command_remove_10 ="rm "+p_5_filename+""
command_remove_11 ="rm log"
command_remove_12 ="rm -r libudf"
command_remove_13 ="rm *.m"

os.system(command_remove_1)
os.system(command_remove_2)
os.system(command_remove_3)
os.system(command_remove_4)
os.system(command_remove_5)
os.system(command_remove_6)
os.system(command_remove_7)
os.system(command_remove_8)
os.system(command_remove_9)
os.system(command_remove_10)
os.system(command_remove_11)
os.system(command_remove_12)
os.system(command_remove_13)

### compress files

command_1 ="tar -cvzf Fluent_"+fluent_file_name+".tar.gz "+fluent_file_name+".cas " +fluent_file_name+".dat "
command_2 = "rm *.cas"
command_3 = "rm *.dat"
command_4 ="tar -cvzf Flow_field_"+fluent_file_name+".tar.gz  *.csv"
command_5 = "rm *.csv"

os.system(command_1)
os.system(command_2)
os.system(command_3)
os.system(command_4)
os.system(command_5)


