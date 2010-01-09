%% log
% 080911  Analytical solution for general nondry hL and hR
% 080911a Updated generalized limiter 
% 080912  Phase speed based alpha implemented
% 080912a Plot shows courant number
% 080912b irregular dx implemented
% 080915  xp and xpi corrected for value at center 
% 080915b height & flow (h & hwu) formation with rectangular channel (varied width) implemented 
% 080916  Friction with Manning's n 
% 080916a Check findroot.m when dambreak analytical solution behaves weird
%         Bottom Elevation at interface implemented (BotE_i)
%         Changed X length scale
% 081004  volume index (10:ni)  interface index (9:ni)
%         ghost volume (8:9) and (ni+1:ni+2)
% 081025  delete index 1:7 and ni+3: 
%         delete interface index 1:7 and ni+2:
%         keep ghost volume (8:9) and (ni+1:ni+2)
% 081025a load dxr data
%         draw grid illustration. check grid.pdf or grid.ai
%         to load elevation data and 
% 081026  load w (volume average) and w_i (interface w)
%         volume index starts from 11 to ni
%         ghost volume (9:10) and (ni+1:ni+2)
% 081027  elevation computing corrected
%         steady-state non-flat bottom tested
% 081028  smoothing acceleration for steady-state( courant # > 10 )
%         search "Smoothing for steady-state acceleration"
% 081028a load data from text file
% 081028b write elevation data for steady-state test 2 case
%         to load elevation data from text file. check
%         "Elevation_MacDonald_Test2.m"
% 081028c load elevation data implemented
%         to load xpi instead of dxr. change xpi(9:ni+1) to xpi(8:ni+2)
% 081029  load xpi data implemented
% 081029a to seperate different test cases
% 081031  wrote external functions for initial, boundary conditions, and
%         phase speed calculation
% 081031a external functions for plot
%         seperated test cases
% 081101  some plot bugs corrected  
% 081101a switch case instead of strcmp
% 081101b implemented test case Khalifa 1980
% 081101c added test case Liang 2008 and Zhou 2001
%         check folder data_Zhou2001 and data_Liang2008
% 081202  improved plot_1.m to include u plot
%         to implement non-reflected boundary condition
% 081205  non-reflected boundary condition successfully implemented.
%         see boundary_condition_non_reflected_bc_Sanders.m
% 081205a to implement flow network
% 081218  to implement specified_bc
% 081218a implemented specified_bc
% 090209  updated specified_bc
% 090209a implemented specified_bc_both_h_u
% 090210  Corrected boundary condition mistakes in 090209a
%         To try network. See KC1D_network.m
% 090714  retry by building testing cases.
% 090715  fixed xp error in geometry_initial_MacDonald2.
% 090728  generalized dambreak case.

%%
function oneD

%% Parameters
clear
g=9.81;
t=0;

%test_case = 'specified_bc_both_h_u';
%test_case = 'specified_bc';
%test_case = 'non_reflected_bc';
test_case = 'dambreak';
%test_case = 'macdonald2';
%test_case = 'Khalifa1980';
illustrate=1;  % 1:plot h  2:plot u
sc='Analytical';
legend_position = 3;
%plot_ylim = [0 10]; %auto
plot_ylim = 'auto';

%% parameters for each test case
switch lower(test_case)
    case('specified_bc_both_h_u')
        number_of_volume_data = 24; % number of volume includes 2*2 ghost cells

        Manning_n = 0;
        dt = 0.5;
        t_end=800;
        hl=10;
        hr=5;
        S=findroot(hl,hr);
        plot_options = 'both'; 
    case('specified_bc')
        number_of_volume_data = 24; % number of volume includes 2*2 ghost cells

        Manning_n = 0;
        dt = 0.5;
        t_end=80;
        hl=10;
        hr=5;
        S=findroot(hl,hr);
        plot_options = 'both';   
    case('non_reflected_bc')
        number_of_volume_data = 24; % number of volume includes 2*2 ghost cells

        Manning_n = 0;
        dt = 0.5;
        t_end=80;
        hl=10;
        hr=5;
        S=findroot(hl,hr);
        plot_options = 'both';
    case('dambreak')
        %moved
    case('macdonald2')
        number_of_volume_data = 24; % number of volume includes 2*2 ghost cells

        Manning_n = 0.02;
        dt = 2;
        t_end=700;
        plot_options = 'both';
    case('khalifa1980')
        number_of_volume_data = 125; % number of volume includes 2*2 ghost cells

        Manning_n = 0.0;
        dt = 0.005;
        t_end=4;
        plot_options = 'numerical';               
    otherwise
        disp('test_case error!!!');
end

%% Initialize - load dxr data, find L, and assign ghost volume dxr
folder_name=['data_' test_case];
switch lower(test_case)
    case('specified_bc_both_h_u')
        ni = number_of_volume_data + 6;
        [L,xpi,xp,xp_delta,xpi_delta,w,w_i,BotE_i]=...
            geometry_initial(number_of_volume_data,ni,folder_name,'data_xpi','data_w','data_wi','data_BotE_i');
        BotE_i(8:ni+2) = 0;

        %overwrite geometry
        number_of_volume_data = 30;
        ni = number_of_volume_data + 6;
        xpi(8)=0;
        for i=9:ni+2
            xpi(i) = xpi(i-1) + 20;
        end        
        [L,xp,xp_delta,xpi_delta,w,w_i,BotE_i]=geometry_initial_2(ni,xpi);
    case('specified_bc')
        ni = number_of_volume_data + 6;
        [L,xpi,xp,xp_delta,xpi_delta,w,w_i,BotE_i]=...
            geometry_initial(number_of_volume_data,ni,folder_name,'data_xpi','data_w','data_wi','data_BotE_i');
        BotE_i(8:ni+2) = 0;

        %overwrite geometry
        number_of_volume_data = 30;
        ni = number_of_volume_data + 6;
        xpi(8)=0;
        for i=9:ni+2
            xpi(i) = xpi(i-1) + 20;
        end        
        [L,xp,xp_delta,xpi_delta,w,w_i,BotE_i]=geometry_initial_2(ni,xpi);
    case('non_reflected_bc')
%         ni = number_of_volume_data + 6;
%         [L,xpi,xp,xp_delta,xpi_delta,w,w_i,BotE_i]=...
%             geometry_initial(number_of_volume_data,ni,folder_name,'data_xpi','data_w','data_wi','data_BotE_i');
%         BotE_i(8:ni+2) = 0;

        %overwrite geometry
        number_of_volume_data = 30;
        ni = number_of_volume_data + 6;
        xpi(8)=0;
        for i=9:ni+2
            xpi(i) = xpi(i-1) + 20;
        end        
        [L,xp,xp_delta,xpi_delta,w,w_i,BotE_i]=geometry_initial_2(ni,xpi);
        
    case('dambreak')
%         ni = number_of_volume_data + 6;
%         [L,xpi,xp,xp_delta,xpi_delta,w,w_i,BotE_i]=...
%             geometry_initial(number_of_volume_data,ni,folder_name,'data_xpi','data_w','data_wi','data_BotE_i');
%         BotE_i(8:ni+2) = 0;

        %overwrite geometry
%         number_of_volume_data = 50;
%         ni = number_of_volume_data + 6;

        n_cell  = 26;
        n_ghost =  2;
        i_begin = 11;
        i_end   = i_begin + n_cell - 1;
        
        i_g_begin =  i_begin - n_ghost;
        i_g_end   =  i_end   + n_ghost; 
        
        
        %number_of_volume_data = 30;  % number of volume includes 2*2 ghost cells
        %ni = number_of_volume_data + 6;

        Manning_n = 0;
        dt = 0.8;
        t_end=65;
        hl=10;
        hr=5;
        S=findroot(hl,hr);
        plot_options = 'both';
        
        xpi(i_g_begin - 1) = 0;
        for i = i_g_begin : i_g_end
            xpi(i) = xpi(i-1) + 20 + 60*mod(i,3);
        end

        [L,xp,xp_delta,xpi_delta,w,w_i,BotE_i] = geometry_initial_2(xpi,i_begin,i_end,i_g_begin,i_g_end,n_ghost);
        
        [x_exact,h_exact,u_exact] = exact_dambreak(S,t,g,hr,hl,L); % call exact solution
        [h(i_g_begin:i_g_end),u(i_g_begin:i_g_end)]=initial_condition_dambreak(xp(i_g_begin:i_g_end),hr,hl,L);
        %plot initial 
        clf;
        plot_initial_condition_both(sc,illustrate,xp(i_begin:i_end),h(i_begin:i_end),u(i_begin:i_end),x_exact,h_exact,u_exact)
        hold off; M=getframe(gcf);
         
    case('macdonald2')
        ni = number_of_volume_data + 6;
        [L,xpi,xp,xp_delta,xpi_delta,w,w_i,BotE_i]=...
            geometry_initial_MacDonald2(number_of_volume_data,ni,folder_name,'data_xpi','data_w','data_wi','data_BotE_i');
    case('khalifa1980')
        ni = number_of_volume_data + 6;
        [L,xpi,xp,xp_delta,xpi_delta,w,w_i,BotE_i]=...
            geometry_initial(number_of_volume_data,ni,folder_name,'data_xpi','data_w','data_wi','data_BotE_i');
        
    otherwise
        disp('test_case error!!!');
end

%% Initial Conditions
switch lower(test_case)
    case('specified_bc_both_h_u')
        [x_exact,h_exact,u_exact] = exact_dambreak(S,t,g,hr,hl,L); % call exact solution
        [h(9:ni+2),u(9:ni+2)]=initial_condition_dambreak(xp(9:ni+2),hr,hl,L);
        %plot initial 
        clf;
        plot_initial_condition_both(sc,illustrate,xp(11:ni),h(11:ni),u(11:ni),x_exact,h_exact,u_exact)
        hold off; M=getframe(gcf);
    case('specified_bc')
        [x_exact,h_exact,u_exact] = exact_dambreak(S,t,g,hr,hl,L); % call exact solution
        [h(9:ni+2),u(9:ni+2)]=initial_condition_dambreak(xp(9:ni+2),hr,hl,L);
        %plot initial 
        clf;
        plot_initial_condition_both(sc,illustrate,xp(11:ni),h(11:ni),u(11:ni),x_exact,h_exact,u_exact)
        hold off; M=getframe(gcf);
    case('non_reflected_bc')
        [x_exact,h_exact,u_exact] = exact_dambreak(S,t,g,hr,hl,L); % call exact solution
        [h(9:ni+2),u(9:ni+2)]=initial_condition_dambreak(xp(9:ni+2),hr,hl,L);
        %plot initial 
        clf;
        plot_initial_condition_both(sc,illustrate,xp(11:ni),h(11:ni),u(11:ni),x_exact,h_exact,u_exact)
        hold off; M=getframe(gcf);
    case('dambreak')
        % moved
    case('macdonald2')
        for i=1:1001
            x_exact(i) = i-1;
        end
        [h_exact,u_exact]    =initial_condition_MacDonald_case2(x_exact);
        [h(9:ni+2),u(9:ni+2)]=initial_condition_MacDonald_case2(xp(9:ni+2));
        u(11:ni) = 0;
        %plot initial
        clf
        plot_initial_condition_both(sc,illustrate,xp(9:ni+2),h(9:ni+2),u(9:ni+2),x_exact,h_exact,u_exact)
        hold off; M=getframe(gcf);
    case('khalifa1980')
        [h(9:ni+2),u(9:ni+2)]=initial_condition_Khalifa1980(xp(9:ni+2),w(9:ni+2));

    otherwise
        disp('test_case error!!!');
end

%% Time integration

unst=0;
j=1;
while (t<t_end && unst~=1) % time integration
    
%% Phase Speed % include one neighboring ghost cell

[alpha,courant]=phase_speed(i_end,xpi_delta,g,dt,h,u);

%% Time increment    
   t=t+dt;
   j=j+1;
   %s=dt/dx;

%% cell average area
hw(i_g_begin:i_g_end) = h(i_g_begin:i_g_end).* w(i_g_begin:i_g_end);
hwu(i_g_begin:i_g_end) = h(i_g_begin:i_g_end) .* w(i_g_begin:i_g_end) .* u(i_g_begin:i_g_end);

%% manning's friction

%Rh = A/P 
% P = 2*h + B
%Sf = v^2 * n^2 / R^(4/3)
for i=11:i_end
    P(i) = 2*h(i)+w(i);
    Rh(i) = hw(i)/P(i);
    Sf(i) = u(i)^2 * Manning_n^2/ Rh(i)^(4./3);
end

%% interface limiter
% MUSCL or higher order
% Construct R and L of interface, using h & hwu as independent variables instead of h & u
    %for i=10:ni % using h(9:ni+2) xp_delta(9:ni+1)
    for i = i_begin - 1 : i_end            
        delta_h_R(i) = limiter(   (h(i+2)-h(i+1))/xp_delta(i+1), (h(i+1)-h(i))/xp_delta(i) );
        delta_h_L(i) = limiter(   (h(i)  -h(i-1))/xp_delta(i-1), (h(i+1)-h(i))/xp_delta(i) );           

        h_i_R(i) =   max( h(i+1) - 0.5*delta_h_R(i)*xpi_delta(i+1),  0 );
        h_i_L(i) =   max( h(i)   + 0.5*delta_h_L(i)*xpi_delta(i)  ,  0 );

        hw_i_R(i) =   h_i_R(i)*w_i(i);
        hw_i_L(i) =   h_i_L(i)*w_i(i);
        
        delta_hwu_R(i) = limiter(   (hwu(i+2)-hwu(i+1))/xp_delta(i+1), (hwu(i+1)-hwu(i))/xp_delta(i) );
        delta_hwu_L(i) = limiter(   (hwu(i)  -hwu(i-1))/xp_delta(i-1), (hwu(i+1)-hwu(i))/xp_delta(i) );                  
        
        hwu_i_R(i) =   hwu(i+1) - 0.5*delta_hwu_R(i)*xpi_delta(i+1);
        hwu_i_L(i) =   hwu(i)   + 0.5*delta_hwu_L(i)*xpi_delta(i);        

        if h_i_R(i)>0.0001
        
           hwuu_i_R(i) =  hwu_i_R(i)^2/hw_i_R(i);
        else
           hwuu_i_R(i) = 0; 
        end
        if h_i_L(i)>0.0001
            hwuu_i_L(i) =  hwu_i_L(i)^2/hw_i_L(i);
        else 
            hwuu_i_L(i) = 0;
        end   
   end
          
%% Interface value   
%  i interface for i and i+1 % (10:11) to (ni:ni+1)
    for i = i_begin - 1 : i_end   

         h_i(i) =   0.5* ( h_i_R(i) + h_i_L(i) );
         eta_i(i) =   h_i(i)+BotE_i(i);
         hwu_i(i) =    0.5* ( hwu_i_R(i)  + hwu_i_L(i) );
         hwuu_i(i) =   0.5* ( hwuu_i_R(i) + hwuu_i_L(i) );
        
         
         Dh_i(i) =   -0.5* alpha(i) *( h_i_R(i)  - h_i_L(i) );
         Dhwu_i(i) =  -0.5* alpha(i) *( hwu_i_R(i) - hwu_i_L(i) );        

   end
   

    
%% Lax-Friedrich scheme
% % Smoothing old value for Lax-Friedrich scheme 
%  p1 = 0.5; 
%  p2 = 0.;
%  p3 = 0.5;
%    for i=10:ni
% 
%        h_s(i) = p1* h(i+1) + p2*h(i) + p3*h(i-1) ;
%        hu_s(i) = p1* hu(i+1) + p2*hu(i) + p3*hu(i-1) ;       
%            
%    end
%    
% % lax-Friedrich scheme   
%    for i=10:ni   
%        
%         h_new(i)=h_s(i)- dt/dx*( hu_i(i)-hu_i(i-1));
%                           
%         hu_new(i)= hu_s(i) - ...
%                dt/dx * (  huu_i(i) - huu_i(i-1) ) - ...  % d(huu)
%                dt/dx * g * h_s(i)*( h_i(i) - h_i(i-1) );     % gh * dh           
%                                        
%    end

%% ENO scheme part 1 
%(modified  gh*dh/dx) 

     for i = i_begin : i_end 
        
        h_new(i)=h(i) - dt/(xpi_delta(i)*w(i))*(  hwu_i(i) - hwu_i(i-1) ) - dt/xpi_delta(i)*( Dh_i(i) -Dh_i(i-1) )   ;          
                            
%         hwu_new(i)= hwu(i) - ...
%                dt/xpi_delta(i) * (  hwuu_i(i) - hwuu_i(i-1) ) - ...  % d(huu)
%                dt/xpi_delta(i) * g * hw(i)*( h_i(i) - h_i(i-1) ) - ...     % gh * dh 
%                dt/xpi_delta(i) * (  Dhwu_i(i) - Dhwu_i(i-1) );

        hwu_new(i)= hwu(i) - ...
               dt/xpi_delta(i) * (  hwuu_i(i) - hwuu_i(i-1) ) - ...  % d(huu)
               dt * g * hw(i)*( (eta_i(i) - eta_i(i-1))/xpi_delta(i) + Sf(i) ) - ...     % -gh * (d eta/dx+Sf) 
               dt/xpi_delta(i) * (  Dhwu_i(i) - Dhwu_i(i-1) ); 
    end


               
%% ENO scheme part 2 
%(modified  gh*dh/dx)           
     for i = i_begin : i_end           
           hw_new(i) = h_new(i)*w(i);
           if h_new(i)>0.0001
               u_new(i) = hwu_new(i)/hw_new(i) ;
           else
               u_new(i) = 0;
           end
     end
   h=h_new;
   u=u_new;
   hwu = hwu_new;   

%% Boundary Conditions
switch lower(test_case)
    case('specified_bc_both_h_u')
        h(9:10) = 10;
        u(9:10) = 0;
        h(ni+1:ni+2) = 5;
        u(ni+1:ni+2) = 0;        
    case('specified_bc')
        %[OUT_h_or_u(9:10),hwu(9:10)]=boundary_condition_specified_bc(nb,w,h_L,u_L,h_R,u_R,inner_is_R_or_L,specify_h_or_u)
        bc_u_L = 0;
        u(9:10)=bc_u_L;
        nb=2;
        [h(9:10),hwu(9:10)]=specified_bc(nb,w(9:10),'na',bc_u_L,h(11),u(11),'R','u');
        bc_h_R = 5;
        h(ni+1:ni+2)=bc_h_R;
        [u(ni+1:ni+2),hwu(ni+1:ni+2)]=specified_bc(nb,w(ni+1:ni+2),h(ni),u(ni),bc_h_R,'na','L','h');            
        %bc_u_R = 0;
        %u(ni+1:ni+2)=bc_u_R;
        %[h(ni+1:ni+2),hwu(ni+1:ni+2)]=specified_bc(xp(ni+1:ni+2),w(ni+1:ni+2),h(ni),u(ni),'na',bc_u_R,'L','u');
    case('non_reflected_bc')
        [h(9:10),u(9:10),hwu(9:10)]=boundary_condition_non_reflected_bc_Sanders(xp(9:10),w(9:10),10,0,h(11),u(11));
        [h(ni+1:ni+2),u(ni+1:ni+2),hwu(ni+1:ni+2)]=boundary_condition_non_reflected_bc_Sanders(xp(ni+1:ni+2),w(ni+1:ni+2),h(ni),u(ni),5,0);            
    case('dambreak')
        %[h(9:10),u(9:10),hwu(9:10)]=boundary_condition_dambreak(xp(9:10),w(9:10),hl,0);
        %[h(ni+1:ni+2),u(ni+1:ni+2),hwu(ni+1:ni+2)]=boundary_condition_dambreak(xp(ni+1:ni+2),w(ni+1:ni+2),hr,0);
         h(i_g_begin:i_g_begin+1) = hl;
         u(i_g_begin:i_g_begin+1) = 0;
         hwu(i_g_begin:i_g_begin+1) = h(i_g_begin:i_g_begin+1).*w(i_g_begin:i_g_begin+1).*u(i_g_begin:i_g_begin+1);
         h(i_g_end-1:i_g_end) = hr;
         u(i_g_end-1:i_g_end) = 0;
         hwu(i_g_end-1:i_g_end) = h(i_g_end-1:i_g_end).*w(i_g_end-1:i_g_end).*u(i_g_end-1:i_g_end);
        
        
    case('macdonald2')
        [h(9:10),u(9:10),hwu(9:10)]=boundary_condition_MacDonald_case2(xp(9:10),w(9:10));
        [h(ni+1:ni+2),u(ni+1:ni+2),hwu(ni+1:ni+2)]=boundary_condition_MacDonald_case2(xp(ni+1:ni+2),w(ni+1:ni+2));
    case('khalifa1980')
        [h(9:10),u(9:10),hwu(9:10)]=boundary_condition_Khalifa1980(xp(9:10),w(9:10));
        [h(ni+1:ni+2),u(ni+1:ni+2),hwu(ni+1:ni+2)]=boundary_condition_Khalifa1980(xp(ni+1:ni+2),w(ni+1:ni+2));
    otherwise
        disp('test_case error!!!');
end

%% update exact value for unsteady-state dambreak plot

switch lower(test_case)
    case('specified_bc_both_h_u')
        [x_exact,h_exact,u_exact] = exact_dambreak(S,t,g,hr,hl,L); % call exact solution
    case('specified_bc')
        [x_exact,h_exact,u_exact] = exact_dambreak(S,t,g,hr,hl,L); % call exact solution 
    case('non_reflected_bc')
        [x_exact,h_exact,u_exact] = exact_dambreak(S,t,g,hr,hl,L); % call exact solution    
    case('dambreak')
        [x_exact,h_exact,u_exact] = exact_dambreak(S,t,g,hr,hl,L); % call exact solution
    otherwise
        
end



%% plot interface
    if illustrate==1  % 1:plot h  2:plot u
        plot_interface(illustrate,xpi(i_begin-1:i_end),h_i(i_begin-1:i_end));
    end
%% plot
switch lower(plot_options)
    case('both')
        plot_1(illustrate,sc,t,courant,x_exact  ,h_exact, u_exact ,'r',legend_position  )
        hold on;
        plot_1(illustrate,sc,t,courant,xp(i_g_begin:i_g_end),h(i_g_begin:i_g_end),u(i_g_begin:i_g_end) ,'-ob',legend_position )
        ylim(plot_ylim) 
        hold off; M=getframe(gcf);
    case('numerical')
        plot_1(illustrate,sc,t,courant,xp(i_g_begin:i_g_end),h(i_g_begin:i_g_end),u(i_g_begin:i_g_end) ,'-ob',legend_position )
        ylim(plot_ylim) 
        hold off; M=getframe(gcf);
    otherwise
        disp('test_case error!!!');
end



end

