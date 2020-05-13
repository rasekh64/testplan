clc
clear all


reed_type= input('reed type:')

if reed_type==8
    load points_8.mat;
    lable = {'1', '2', '3', '4', '5', '6','7', ...
    '8', '9' ,'10', '11', '12', '13', '14', ...
    '15', '16'}; 
else
    load points_1.mat;
    lable = {'1', '2', '3', '4', '5', '6','7', ...
    '8', '9' ,'10', '11', '12', '13', '14', ...
    '16'};
end


%%%%%% read points coordinate

point = coordinate(: , 1);
y = coordinate(: , 2);
z = coordinate(:, 3); 

% lable = {'1', '2', '3', '4', '5', '6','7', ...
%     '8', '9' ,'10', '11', '12', '13', '14', ...
%     '15'};

%%% the name of the set up

i = input('the name of setup = ')
speed =  input('yarn speed is = ')

setup_dir = ['/cfdfile2/data/fm/alireza/EcoFlow/Test_plan/setup_',num2str(i),'']; 
cd(setup_dir)

%%%%%% force data

force_file = ['net_force_per_lenght_point_setup_',num2str(i),'_yarn_speed_',num2str(speed),'.txt']

fileID = fopen(force_file,'r');
a = textscan(fileID, '%s %f %f %f', [4 inf]);
a = a';
fclose(fileID)

f_x= a{2,:};
f_y= a{3,:};
f_z= -1*a{4,:};


[y_f,z_f] = meshgrid(-6:0.05:0, 0:0.05:6);
force_x= griddata(y,z,f_x,y_f,z_f);
force_y= griddata(y,z,f_y,y_f,z_f);
force_z= griddata(y,z,f_z,y_f,z_f);
% 
% 
figure
mesh(y_f, z_f, force_x)
caxis([0 700])
% caxis([0 200])


xlabel('y(mm)','FontSize',16)
ylabel('z(mm)','FontSize',16)
zlabel('Force_x (mN/m)', 'FontSize',12,'FontWeight','bold')
title('F_x per yarn lenght (mN/m)', 'FontSize',16,'FontWeight','bold')
set(gca,'FontSize',16)
colorbar
view(90, -90)
hold on
plot3(y,z, f_x, 'o','MarkerFaceColor',[0 0 0])
text(y,z, lable, 'FontSize',16)
hold off
fig_x_name = ['fx_setup_',num2str(i), '_speed_', num2str(speed), '.tif']
saveas(gcf,fig_x_name)

 
figure
mesh(y_f, z_f, force_y)
% caxis([0 300])
caxis([0 700])


xlabel('y(mm)','FontSize',16)
ylabel('z(mm)','FontSize',16)
zlabel('Force_y (mN/m)', 'FontSize',16,'FontWeight','bold')
title('F_y per yarn lenght (mN/m)', 'FontSize',16,'FontWeight','bold')
set(gca,'FontSize',16)
colorbar
view(90, -90)
hold on
plot3(y,z, f_y, 'o','MarkerFaceColor',[0 0 0])
text(y,z, lable, 'FontSize',16)
hold off
fig_y_name = ['fy_setup_',num2str(i), '_speed_', num2str(speed), '.tif']
saveas(gcf,fig_y_name)
% 
% 
figure
mesh(y_f, z_f, force_z)
% caxis([200 700])
caxis([200 1100])

xlabel('y(mm)','FontSize',16)
ylabel('z(mm)','FontSize',16)
zlabel('Force_z (mN/m)', 'FontSize',12,'FontWeight','bold')
title('F_z per yarn lenght (mN/m)', 'FontSize',16,'FontWeight','bold')
set(gca,'FontSize',16)
colorbar
view(90, -90)
hold on
plot3(y,z, f_z, 'o','MarkerFaceColor',[0 0 0])
text(y,z, lable, 'FontSize',16)
hold off
fig_z_name = ['fz_setup_',num2str(i), '_speed_', num2str(speed), '.tif']
saveas(gcf,fig_z_name)



