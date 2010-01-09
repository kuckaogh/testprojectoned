function residual = shock_nondry(S,hL,hR)
g=9.81;
%hL=1;
%hR=0.5;
%S=2*sqrt(g*hL)+g*hR/(4*S)*(1+sqrt(1+8*S^2/(g*hR))) - sqrt(2*g*hR*sqrt(1+8*S^2/(g*hR)) -2*g*hR )

residual=2*sqrt(g*hL)+g*hR/(4*S)*(1+sqrt(1+8*S^2/(g*hR))) - sqrt(2*g*hR*sqrt(1+8*S^2/(g*hR)) -2*g*hR )-S;
end




