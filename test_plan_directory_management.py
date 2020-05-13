import os

# directory is changed to the directory of the test plan":

test_plan_dir = "/cfdfile2/data/fm/alireza/EcoFlow/Test_plan/"
os.chdir(test_plan_dir)
top_dir= os.getcwd()
print(top_dir)


###########################

# for i in range(1, 26):
#     os.chdir(test_plan_dir)
#     top_dir = os.getcwd()
#     folder_name_1 = "setup_" + str(i)
#     print(folder_name_1)
#     os.mkdir(folder_name_1)
#     folder_dir_1 = top_dir + "/" + folder_name_1 + "/"
#     print(folder_dir_1)
#
#     #subfolders 1:
#     for j in range(1, 16):
#         os.chdir(folder_dir_1)
#         sub_folder_1_dir = os.getcwd()
#         folder_name_2 = "setup_" + str(i)+"_yarn_position_" + str(j)
#         os.mkdir(folder_name_2)
#         folder_dir_2 = sub_folder_1_dir + "/" + folder_name_2 + "/"
#         print(folder_dir_2)
#         # subfolders 2:
#
#         for k in range(60, 120, 30):
#             os.chdir(folder_dir_2)
#             sub_folder_2_dir = os.getcwd()
#             folder_name_3 = "setup_" + str(i)+"_yarn_position_" + str(j)+"_yarn_speed_" + str(k)
#             os.mkdir(folder_name_3)
#             folder_dir_3 = sub_folder_2_dir + "/" + folder_name_3 + "/"
#             print(folder_dir_3)

# for i in range(26, 28):
#     os.chdir(test_plan_dir)
#     top_dir = os.getcwd()
#     folder_name_1 = "setup_" + str(i)
#     print(folder_name_1)
#     os.mkdir(folder_name_1)
#     folder_dir_1 = top_dir + "/" + folder_name_1 + "/"
#     print(folder_dir_1)
#
#     #subfolders 1:
#     for j in range(1, 16):
#         os.chdir(folder_dir_1)
#         sub_folder_1_dir = os.getcwd()
#         folder_name_2 = "setup_" + str(i)+"_yarn_position_" + str(j)
#         os.mkdir(folder_name_2)
#         folder_dir_2 = sub_folder_1_dir + "/" + folder_name_2 + "/"
#         print(folder_dir_2)
#         # subfolders 2:
#
#         for k in range(60, 120, 30):
#             os.chdir(folder_dir_2)
#             sub_folder_2_dir = os.getcwd()
#             folder_name_3 = "setup_" + str(i)+"_yarn_position_" + str(j)+"_yarn_speed_" + str(k)
#             os.mkdir(folder_name_3)
#             folder_dir_3 = sub_folder_2_dir + "/" + folder_name_3 + "/"
#             print(folder_dir_3)


for i in range(20, 26):
    os.chdir(test_plan_dir)
    top_dir = os.getcwd()
    folder_name_1 = "setup_" + str(i)
    # print(folder_name_1)
    # os.mkdir(folder_name_1)
    folder_dir_1 = top_dir + "/" + folder_name_1 + "/"
    print(folder_dir_1)

    #subfolders 1:
    # for j in range(1, 16):
    j=16
    os.chdir(folder_dir_1)
    sub_folder_1_dir = os.getcwd()
    folder_name_2 = "setup_" + str(i)+"_yarn_position_" + str(j)
    os.mkdir(folder_name_2)
    folder_dir_2 = sub_folder_1_dir + "/" + folder_name_2 + "/"
    print(folder_dir_2)
    # subfolders 2:

    for k in range(60, 120, 30):
        os.chdir(folder_dir_2)
        sub_folder_2_dir = os.getcwd()
        folder_name_3 = "setup_" + str(i)+"_yarn_position_" + str(j)+"_yarn_speed_" + str(k)
        os.mkdir(folder_name_3)
        folder_dir_3 = sub_folder_2_dir + "/" + folder_name_3 + "/"
        print(folder_dir_3)



