clc
clear all

reed_type= input('reed type:')

if reed_type==8
    load points_8.mat;
else
    load points_1.mat;
end


%%%%%% read points coordinate

point = coordinate(: , 1);
y = coordinate(: , 2);
z = coordinate(:, 3); 

lable = {'1', '2', '3', '4', '5', '6','7', ...
    '8', '9' ,'10', '11', '12', '13', '14', ...
    '15'};

%%% the name of the set up

i = input('the name of setup = ')
speed_i =  input('yarn speed is = ')
setup_dir_i = ['/cfdfile2/data/fm/alireza/EcoFlow/Test_plan/setup_',num2str(i),'']; 
cd(setup_dir_i)

%%%%%% force data

force_file_i = ['net_force_per_lenght_point_setup_',num2str(i),'_yarn_speed_',num2str(speed_i),'.txt']

f_i = fopen(force_file_i,'r');
a_i = textscan(f_i, '%s %f %f %f', [4 inf]);
a_i = a_i';
fclose(f_i)

f_x_i= a_i{2,:};
f_y_i= a_i{3,:};
f_z_i= -1*a_i{4,:};
%%%%%%%%%%%%%%%

j = input('the name of setup = ')
speed_j =  input('yarn speed is = ')
setup_dir_j = ['/cfdfile2/data/fm/alireza/EcoFlow/Test_plan/setup_',num2str(j),'']; 
cd(setup_dir_j)

%%%%%% force data

force_file_j = ['net_force_per_lenght_point_setup_',num2str(j),'_yarn_speed_',num2str(speed_j),'.txt']

f_j = fopen(force_file_j,'r');
a_j = textscan(f_j, '%s %f %f %f', [4 inf]);
a_j = a_j';
fclose(f_j)

f_x_j= a_j{2,:};
f_y_j= a_j{3,:};
f_z_j= -1*a_j{4,:};

f_x_r = f_x_i./f_x_j;
f_y_r = f_y_i./f_y_j;
f_z_r = f_y_i./f_y_j;


[y_f,z_f] = meshgrid(-6:0.05:0, 0:0.05:6);
force_x= griddata(y,z,f_x_r,y_f,z_f);
force_y= griddata(y,z,f_y_r,y_f,z_f);
force_z= griddata(y,z,f_z_r,y_f,z_f);
% 
% 
figure
mesh(y_f, z_f, force_x)
% caxis([0.5 2])
xlabel('y(mm)','FontSize',16)
ylabel('z(mm)','FontSize',16)
zlabel('Force_x (mN/m)', 'FontSize',12,'FontWeight','bold')
title('F_x per yarn lenght (mN/m)', 'FontSize',16,'FontWeight','bold')
set(gca,'FontSize',16)
colorbar
view(90, -90)
hold on
plot3(y,z, f_x_r, 'o','MarkerFaceColor',[0 0 0])
text(y,z, lable, 'FontSize',16)
hold off
fig_x_name = ['fx_setup_11_12.tif']
saveas(gcf,fig_x_name)

 
figure
mesh(y_f, z_f, force_y)
% caxis([1 2])

xlabel('y(mm)','FontSize',16)
ylabel('z(mm)','FontSize',16)
zlabel('Force_y (mN/m)', 'FontSize',16,'FontWeight','bold')
title('F_y per yarn lenght (mN/m)', 'FontSize',16,'FontWeight','bold')
set(gca,'FontSize',16)
colorbar
view(90, -90)
hold on
plot3(y,z, f_y_r, 'o','MarkerFaceColor',[0 0 0])
text(y,z, lable, 'FontSize',16)
hold off
fig_y_name = ['fy_setup_11_12.tif']
saveas(gcf,fig_y_name)
% 
% 
figure
mesh(y_f, z_f, force_z)
% caxis([1 2])
xlabel('y(mm)','FontSize',16)
ylabel('z(mm)','FontSize',16)
zlabel('Force_z (mN/m)', 'FontSize',12,'FontWeight','bold')
title('F_z per yarn lenght (mN/m)', 'FontSize',16,'FontWeight','bold')
set(gca,'FontSize',16)
colorbar
view(90, -90)
hold on
plot3(y,z, f_z_r, 'o','MarkerFaceColor',[0 0 0])
text(y,z, lable, 'FontSize',16)
hold off
fig_z_name = ['fz_setup_11_12.tif']
saveas(gcf,fig_z_name)



