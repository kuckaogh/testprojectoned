%generalized monotonized ventral(MC), Van Leer 1977
% and UMIST, Lien & Leschziner 1994

%phi(r) = max{ 0, min[ 2r, a+(1-a)*r, (a-1)+a*r, beta ] }
% where r = [ u(i) - u(i-1) ]/[ u(i+1) - u(i) ]
% 1 <= beta <= 2
% 0 <= a    <= 1


function Z = limiter(L,R)

beta = 1.5;
ave1 = abs(0.5*(L+R));
%ave2 = abs(0.25*L+0.75*R);
%ave3 = abs(0.75*L+0.25*R);
if (L*R <= 0)
    Z = 0;
elseif (abs(L)>abs(R))
    Z = sign(L)*min([abs(L),beta*abs(R),ave1]);

elseif (abs(R)>abs(L))
    Z = sign(L)*min([abs(R),beta*abs(L),ave1]);

else % abs(R) = abs(L)
    Z = R;
end


