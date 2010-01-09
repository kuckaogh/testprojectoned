function [alpha,courant]=phase_speed(ni,dxr,g,dt,h,u)
%% Phase Speed % include one neighboring ghost cell

for i=10:ni+1
   Cp(i) = u(i) + sqrt(g*h(i));
   Cm(i) = u(i) - sqrt(g*h(i));
   C(i) = max( abs(Cp(i)), abs(Cm(i)) );
end
for i=10:ni
        
   C_i(i) = max( C(i), C(i+1) ); % interface  
   %alpha(i) = 0.9*dx/dt;
end
C_max = max(C_i);
gamma = min(dxr(10:ni+1)/dt);   
courant = C_max/gamma;   
span = 3; % Size of the averaging window
window = ones(span,1)/span; 
alpha_smooth = max(convn(C_i,window,'same'),C_i);
alpha = max(1.0*alpha_smooth,gamma*0);
%alpha(9:ni+1) = gamma;