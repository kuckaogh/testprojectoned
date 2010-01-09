function [L,xp,xp_delta,xpi_delta,w,w_i,BotE_i]=...
    geometry_initial_2(xpi,i_begin,i_end,i_g_begin,i_g_end,n_ghost)


for i = i_g_begin : i_g_end
    xpi_delta(i) = xpi(i) - xpi(i-1);
end

for i = i_g_begin : i_g_end
   %xp(i) = sum(dxi(1:i-1))-sum(dxi(1:11-1))+0.5*dxr(11); % index 11 has x>0
   xp(i) = 0.5*(xpi(i-1)+xpi(i));
end

for i=i_g_begin : i_g_end - 1
    xp_delta(i) = xp(i+1)-xp(i);
end

width = 10.0;

w  ( i_g_begin : i_g_end )   = width;
w_i( i_g_begin : i_g_end-1 ) = width;

BotE_i( i_g_begin -1 : i_g_end ) = 0;

L = xpi( i_end ) - xpi( i_begin - 1 );



