function plot_initial_condition_both(sc,illustrate,x,h,u,x_exact,h_exact,u_exact)

if (illustrate ==1)
  plot(x_exact,h_exact,'r')
  hold on 
  plot(x,h,'bo')
  %axis([0 1 0.4 1.1]) 
  %axis([0 L 0 1.2*hl]) 
  xlabel('x')
  ylabel('h(x,t) : t = 0s')
    legend('Exact',sc)
else
  plot(x_exact,u_exact,'r')
  hold on 
  plot(x,u,'b')
  %axis([0 L 0 1.2*hl]) 
  xlabel('x')
  ylabel('u(x,t) : t = 0s')
    legend('Exact',sc,2)
end
