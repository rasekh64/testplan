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
setup_1 = Case("Reed_1", 74, -8.02, 12.03, 6.23, 9.87, 1.6)
setup_2= Case("Reed_2", 74, -8.02, 12.03, 6.23, 9.87, 1.6)
setup_3= Case("Reed_3", 74, -8.02, 12.03, 6.23, 9.87, 1.6)
setup_4= Case("Reed_4", 74, -8.02, 12.03, 6.23, 9.87, 1.6)
setup_5= Case("Reed_1", 74, -8.02, 12.03, 6.23, 10.87, 1.6)
setup_6= Case("Reed_1", 74, -8.02, 12.03, 6.23, 8.87, 1.6)
setup_7= Case("Reed_1", 74, -8.02, 12.03, 7.23, 9.87, 1.6)
setup_8= Case("Reed_1", 74, -8.02, 12.03, 5.23, 9.87, 1.6)
setup_9= Case("Reed_1", 74, -8.02, 12.03, 5.607, 8.883, 1.6)
setup_10= Case("Reed_1", 74, -8.02, 12.03, 6.853, 10.857, 1.6)
setup_11= Case("Reed_1", 60, -8.02, 12.03, 6.23, 9.87, 1.6)
setup_12= Case("Reed_1", 60, -8.02, 12.03, 6.23, 9.87, 1.5)
setup_13= Case("Reed_1", 60, -8.02, 12.03, 5.607, 8.883, 1.5)
setup_14= Case("Reed_1", 60, -8.02, 12.03, 6.853, 10.857, 1.5)
setup_15= Case("Reed_1", 40, -8.02, 12.03, 6.23, 9.87, 1.6)
setup_16= Case("Reed_1", 40, -8.02, 12.03, 6.23, 9.87, 1.3)
setup_17= Case("Reed_1", 40, -8.02, 12.03, 6.23, 9.87, 1.1)
setup_18= Case("Reed_1", 74, -7.11, 11.62, 5.63, 11.23, 1.6)
setup_19= Case("Reed_8", 74, -8.02, 12.03, 6.23, 9.87, 1.6)
setup_20= Case("Reed_8", 60, -8.02, 12.03, 6.23, 9.87, 1.6)
setup_21= Case("Reed_8", 60, -7.689, 9.03, 7.603, 9.356, 1.6)
setup_22= Case("Reed_8", 60, -7.689, 9.03, 6.082, 7.485, 1.6)
setup_23= Case("Reed_8", 40, -7.689, 9.03, 6.082, 7.485, 1.6)
setup_24= Case("Reed_8", 40, -7.689, 9.03, 6.082, 7.485, 1.3)
setup_25= Case("Reed_8", 40, -7.689, 9.03, 6.082, 7.485, 1.1)


#i=input("the setup number is: ")
i=4
point = input("the location of the yarn is: ")
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

######## set the directory

journal_setup_dir = "/cfdfile2/data/fm/alireza/EcoFlow/Test_plan/setup_"+str(i)+"/setup_"+str(i)+"_yarn_position_"+str(point)+"" \
                                    "/setup_"+str(i)+"_yarn_position_"+str(point)+"_yarn_speed_"+str(speed)+""
os.chdir(journal_setup_dir)
direct= os.getcwd()

fluent_name= "setup_"+str(i)+"_position_"+str(point)+"_speed_"+str(speed)+""


command_1 ="tar -cvzf Fluent_"+fluent_name+".tar.gz "+fluent_name+".cas " +fluent_name+".dat "
command_2 = "rm *.cas"
command_3 = "rm *.dat"
command_4 ="tar -cvzf Flow_field_"+fluent_name+".tar.gz  *.csv"
command_5 = "rm *.csv"


os.system(command_1)
os.system(command_2)
os.system(command_3)
os.system(command_4)
os.system(command_5)


