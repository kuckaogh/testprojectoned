function [h,u]=initial_condition_dambreak(x,hr,hl,L)

[dummy,n] = size(x);

for i=1:n
   %xp(i)=(i-10)*dx;

   if (x(i)<0.5*L) 
     h(i)=hl;
   elseif (x(i)==0.5*L)
     h(i)=(hl+hr)/2;
   else
     h(i)=hr;
   end
   u(i)=0;
end