function [xe,h_e,u_e]=exact_dambreak(S,t,g,hr,hl,L)
sq=sqrt(1+8*S^2/g/hr);
u2=S-(g*hr/4/S)*(1+sq);
c2=sqrt(g*hr/2*(sq-1));

xa=0.5*L-t*sqrt(g*hl);
xb=(u2-c2)*t+0.5*L;
xc=S*t+0.5*L;
for i=1:1001
  xe(i)=(i-1)*L/1000; %0.001;
  if (t==0)
    if (xe(i)<=0.5*L) 
      h_e(i)=hl;
    else
      h_e(i)=hr;
    end
    u_e(i)=0;
  else
    if xe(i)<xa
      h_e(i)=hl; 
      u_e(i)=0;
    elseif (xe(i)>=xa && xe(i)<=xb)
      h_e(i)=(2*sqrt(g*hl)-(2*xe(i)-L)/(2*t))^2/(9*g);
      u_e(i)=(2*(xe(i)+t*sqrt(g*hl))-L)/(3*t);
    elseif (xe(i)>xb && xe(i)<=xc)
       h_e(i)=hr*(sq-1)/2;
       u_e(i)=u2;
    elseif xe(i)>xc
       h_e(i)=hr;
       u_e(i)=0;
    end
  end
end
