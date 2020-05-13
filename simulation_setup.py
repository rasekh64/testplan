import os
from math import *
from Case import Case

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

# print(setup_25.beta)
#############################################################
## specify the case number:


# i=input("the setup number is: ")
i=25
point = input("the location of the yarn is: ")
#point = 1
# speed = input("the speed of the yarn is: ")
speed = 60

reed_type = eval("setup_"+str(i)+".reed")
interval = eval("setup_"+str(i)+".interval")
y_n = eval("setup_"+str(i)+".y_n")
z_n= eval("setup_"+str(i)+".z_n")
alpha= eval("setup_" + str(i) + ".alpha")
beta= eval("setup_" + str(i) + ".beta")
diameter= eval("setup_" + str(i) + ".n_diameter")
p_in = eval("setup_" + str(i) + ".p_in")

# speed= eval("setup_" + str(i) + ".speed")
##############################################################
# write the journal file and launch fluent
main_journal_setup_dir = "/cfdfile2/data/fm/alireza/EcoFlow/reed_channel/simulation"
os.chdir(main_journal_setup_dir)
main_direct= os.getcwd()

file_1=open("journal_simulation_setup_reed_test_plan.jou", "r")
file_1_lines = file_1.readlines()

file_1_lines [1] = "(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"/cfdfile2/data/fm/alireza/EcoFlow/" \
                   "reed_channel/mesh/reed_mesh/"+reed_type+"_"+str(interval)+".msh\") \"Mesh Files (*.msh* *.MSH* )\")\n"
file_1_lines [4] = "(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"/cfdfile2/data/fm/alireza/EcoFlow/" \
                   "reed_channel/mesh/nozzle_striaght/"+str(diameter)+"/nozzle-"+str(diameter)+"_a"+str(alpha)+"_b"+str(beta)+"" \
                    "_y"+str(y_n)+"_z"+str(z_n)+"-meduim.msh\") \"Case Files (*.cas* *.msh* *.MSH* )\")\n"

if reed_type == "Reed_8" and point == 9:
    file_1_lines [8] = "(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"/cfdfile2/data/fm/alireza/EcoFlow/reed" \
                   "_channel/mesh/yarn/yarn-0.4-"+str(interval-2)+"mm-point"+str(point)+"-reed8.msh\") \"Case Files (*.cas* *.msh* *.MSH* )\")\n"
elif reed_type == "Reed_8" and point == 13:
    file_1_lines [8] = "(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"/cfdfile2/data/fm/alireza/EcoFlow/reed" \
                    "_channel/mesh/yarn/yarn-0.4-"+str(interval-2)+"mm-point"+str(point)+"-reed8.msh\") \"Case Files (*.cas* *.msh* *.MSH* )\")\n"
else:
    file_1_lines [8] = "(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"/cfdfile2/data/fm/alireza/EcoFlow/reed" \
                   "_channel/mesh/yarn/yarn-0.4-"+str(interval-2)+"mm-point"+str(point)+".msh\") \"Case Files (*.cas* *.msh* *.MSH* )\")\n"
    
fluent_case_dir = "/cfdfile2/data/fm/alireza/EcoFlow/Test_plan/setup_"+str(i)+"/setup_"+str(i)+"_yarn_position_"+str(point)+\
             "/setup_"+str(i)+"_yarn_position_"+str(point)+"_yarn_speed_"+str(speed)+"/setup_"+str(i)+"_position_"+str(point)+"_speed_"+str(speed)+""
file_1_lines [201] = "(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \""+str(fluent_case_dir)+".cas\") \"Case/Data " \
                    "Files (*.cas* *.pdat* )\")\n"

if interval == 60 and reed_type == "Reed_1":
    file_1_lines[77] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|pressure-inlet (pressure-inlet, id=20)\"))\n"
    file_1_lines[78] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|pressure-inlet (pressure-inlet, id=20)\"))\n"
    file_1_lines[80] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|pressure-inlet (pressure-inlet, id=20)\"))\n"
    file_1_lines[49] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Cell Zone Conditions|component-nozzle (fluid, id=23)\"))\n"
    file_1_lines[50] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Cell Zone Conditions|component-nozzle (fluid, id=23)\"))\n"
    file_1_lines[56] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Cell Zone Conditions|yarn-component (fluid, id=29)\"))\n"
    file_1_lines[57] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Cell Zone Conditions|yarn-component (fluid, id=29)\"))\n"
    file_1_lines[123] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|overset-interface (wall, id=21)\"))\n"
    file_1_lines[124] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|overset-interface (wall, id=21)\"))\n"
    file_1_lines[128] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|overset-yarn (wall, id=24)\"))\n"
    file_1_lines[129] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|overset-yarn (wall, id=24)\"))\n"


if diameter == 1.3:
    file_1_lines[56] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Cell Zone Conditions|yarn-component (fluid, id=29)\"))\n"
    file_1_lines[57] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Cell Zone Conditions|yarn-component (fluid, id=29)\"))\n"
    file_1_lines[59] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Cell Zone Conditions|yarn-component (fluid, id=29)\"))\n"
    file_1_lines[128] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|overset-yarn (wall, id=24)\"))\n"
    file_1_lines[129] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|overset-yarn (wall, id=24)\"))\n"

# if interval == 60 and reed_type == "Reed_8":
#     file_1_lines[77] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|pressure-inlet (pressure-inlet, id=18)\"))\n"
#     file_1_lines[78] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|pressure-inlet (pressure-inlet, id=18)\"))\n"
#     file_1_lines[80] = "(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|pressure-inlet (pressure-inlet, id=18)\"))\n"


journal_setup_dir = "/cfdfile2/data/fm/alireza/EcoFlow/Test_plan/setup_"+str(i)+"/setup_"+str(i)+"_yarn_position_"+str(point)+"" \
                                    "/setup_"+str(i)+"_yarn_position_"+str(point)+"_yarn_speed_"+str(speed)+""

os.chdir(journal_setup_dir)
direct= os.getcwd()

fluent_file_name = "setup_"+str(i)+"_position_"+str(point)+"_speed_"+str(speed)+""
journal_setup_name= "journal_simulation_setup_"+str(i)+"_position_"+str(point)+"_speed_"+str(speed)+".jou"

journal_run_name= "journal_simulation_run_setup_"+str(i)+"_position_"+str(point)+"_speed_"+str(speed)+".jou"

fluent_file_name_90 = "setup_"+str(i)+"_position_"+str(point)+"_speed_90"



file_update=open(journal_setup_name, "w")
for lines in file_1_lines:
    file_update.write(lines)
file_update.close()
fluent_command = "fluent 3ddp -i "+journal_setup_name+" -t36"
os.system(fluent_command)

#### write the job script of fluent

os.chdir(main_journal_setup_dir)
main_job=open("job_hpc.sh", "r")
main_job_lines = main_job.readlines()

main_job_lines [2] = "#PBS -N setup_"+str(i)+"_position_"+str(point)+"_speed_"+str(speed)+"\n"
main_job_lines [13] = "CASE_NAME=setup_" + str(i)+"_yarn_position_" + str(point)+"_yarn_speed_" + str(speed)+ "\n"

direct_1 = "/setup_"+str(i)+"/setup_"+str(i)+"_yarn_position_"+str(point)+""
direct_2 = "/setup_"+str(i)+"/setup_"+str(i)+"_yarn_position_"+str(point)+"/setup_"+str(i)+"_yarn_position_"+str(point)+""
main_job_lines [14] = "CASE_PATH=$VSC_DATA_VO_USER/Test_plan"+direct_1+"/$CASE_NAME \n"
main_job_lines [16] = "FLUENT_INPUTFILE="+journal_run_name+"\n"
os.chdir(journal_setup_dir)
direct = os.getcwd()

hpc_job_name = ""+fluent_file_name+".sh"
file_hpc_job = open(hpc_job_name, "w")

for k in main_job_lines:
    file_hpc_job.write(k)
file_hpc_job.close()

#### write the journal file for runnig the simulation

os.chdir(main_journal_setup_dir)

if diameter != 1.1:
    main_journal_run=open("journal_simulation_run_reed_test_plan.jou", "r")
    main_journal_run_lines = main_journal_run.readlines()

    main_journal_run_lines[0] = "file read-case-data "+fluent_file_name+".cas \n"
    main_journal_run_lines[2]= "file write-case-data "+fluent_file_name+".cas \n"
    main_journal_run_lines[10]= "file write-case-data "+fluent_file_name+".cas \n"
    main_journal_run_lines[14]= "file write-case-data "+fluent_file_name+".cas \n"
    main_journal_run_lines[18]= "file write-case-data "+fluent_file_name+".cas \n"
    main_journal_run_lines[22]= "file write-case-data "+fluent_file_name+".cas \n"
    main_journal_run_lines[26]= "file write-case-data "+fluent_file_name+".cas \n"
    main_journal_run_lines[30]= "file write-case-data "+fluent_file_name+".cas \n"
    main_journal_run_lines[34]= "file write-case-data "+fluent_file_name+".cas \n"
    main_journal_run_lines[40]= "file write-case-data "+fluent_file_name+".cas \n"
    main_journal_run_lines[44]= "file write-case-data "+fluent_file_name+".cas \n"
    main_journal_run_lines[50]= "file write-case-data "+fluent_file_name_90+".cas \n"

    if interval == 60 and reed_type == "Reed_1":
        main_journal_run_lines[12] = "define boundary-conditions pressure-inlet 20 yes no 10000 no 10000 no 293 no yes no no yes 5 10 \n"
        main_journal_run_lines[16] = "define boundary-conditions pressure-inlet 20 yes no 100000 no 100000 no 293 no yes no no yes 5 10 \n"
        main_journal_run_lines[20] = "define boundary-conditions pressure-inlet 20 yes no 200000 no 200000 no 293 no yes no no yes 5 10 \n"
        main_journal_run_lines[24] = "define boundary-conditions pressure-inlet 20 yes no 300000 no 300000 no 293 no yes no no yes 5 10 \n"
        main_journal_run_lines[28] = "define boundary-conditions pressure-inlet 20 yes no 400000 no 400000 no 293 no yes no no yes 5 10 \n"
        main_journal_run_lines[32] = "define boundary-conditions pressure-inlet 20 yes no 400000 no 500000 no 293 no yes no no yes 5 10 \n"
        main_journal_run_lines[36] = "define boundary-conditions wall 27 0 no 0 no no no 0 no yes motion-bc-moving no no no no no 60 1 0 0 no no 0.00019 no 0.5 no 1 \n"
        main_journal_run_lines[37] = "define boundary-conditions wall 26 0 no 0 no no no 0 no yes motion-bc-moving no no no no no 60 1 0 0 no no 0 no 0.5 no 1 \n"
        main_journal_run_lines[38] = "define boundary-conditions wall 25 0 no 0 no no no 0 no yes motion-bc-moving no no no no no 60 1 0 0 no no 0 no 0.5 no 1 \n"
        main_journal_run_lines[46] = "define boundary-conditions wall 27 0 no 0 no no no 0 no yes motion-bc-moving no no no no no 90 1 0 0 no no 0.00019 no 0.5 no 1 \n"
        main_journal_run_lines[47] = "define boundary-conditions wall 26 0 no 0 no no no 0 no yes motion-bc-moving no no no no no 90 1 0 0 no no 0 no 0.5 no 1 \n"
        main_journal_run_lines[48] = "define boundary-conditions wall 25 0 no 0 no no no 0 no yes motion-bc-moving no no no no no 90 1 0 0 no no 0 no 0.5 no 1 \n"

    if diameter == 1.3:
        main_journal_run_lines[36] = "define boundary-conditions wall 27 0 no 0 no no no 0 no yes motion-bc-moving no no no no no 60 1 0 0 no no 0.00019 no 0.5 no 1 \n"
        main_journal_run_lines[37] = "define boundary-conditions wall 26 0 no 0 no no no 0 no yes motion-bc-moving no no no no no 60 1 0 0 no no 0 no 0.5 no 1 \n"
        main_journal_run_lines[38] = "define boundary-conditions wall 25 0 no 0 no no no 0 no yes motion-bc-moving no no no no no 60 1 0 0 no no 0 no 0.5 no 1 \n"
        main_journal_run_lines[46] = "define boundary-conditions wall 27 0 no 0 no no no 0 no yes motion-bc-moving no no no no no 90 1 0 0 no no 0.00019 no 0.5 no 1 \n"
        main_journal_run_lines[47] = "define boundary-conditions wall 26 0 no 0 no no no 0 no yes motion-bc-moving no no no no no 90 1 0 0 no no 0 no 0.5 no 1 \n"
        main_journal_run_lines[48] = "define boundary-conditions wall 25 0 no 0 no no no 0 no yes motion-bc-moving no no no no no 90 1 0 0 no no 0 no 0.5 no 1 \n"

    if p_in == 3:
        main_journal_run_lines[28] = " \n"
        main_journal_run_lines[29] = " \n"
        main_journal_run_lines[30] = " \n"
        main_journal_run_lines[31] = " \n"
        main_journal_run_lines[32] = " \n"
        main_journal_run_lines[33] = " \n"
        main_journal_run_lines[34] = " \n"
        main_journal_run_lines[35] = " \n"
else:
    main_journal_run = open("journal_simulation_run_reed_test_plan_d1.1.jou", "r")
    main_journal_run_lines = main_journal_run.readlines()

    main_journal_run_lines[0] = "file read-case-data "+fluent_file_name+".cas \n"
    main_journal_run_lines[38]= "file write-case-data "+fluent_file_name+".cas \n"
    main_journal_run_lines[44]= "file write-case-data "+fluent_file_name_90+".cas \n"


os.chdir(journal_setup_dir)
direct = os.getcwd()

file_run_update = open(journal_run_name, "w")
for jj in main_journal_run_lines:
    file_run_update.write(jj)
file_run_update.close()



##### Get the command to move the file to the hpc

hpc_dir ="vsc41142@login.hpc.ugent.be:/data/gent/vo/000/gvo00010/vsc41142/Test_plan"+direct_1+"/"

trans_command = "scp -r "+direct+" "+hpc_dir+""
print (trans_command)
os.system(trans_command)