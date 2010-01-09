function x = findroot(hL,hR)

%format long
%x0=2.9579; % for hL=1,hR=0.5
x0=9.3538;
hL = 10;
hR = 5;

x = fzero(@(x) shock_nondry(x,hL,hR),x0);