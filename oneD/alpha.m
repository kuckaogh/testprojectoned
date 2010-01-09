function ans = alpha(k,hr,hl,ur,ul,g)

dh=hr-hl;
duh=hr*ur-hl*ul;
uav=(sqrt(hr)*ur+sqrt(hl)*ul)/(sqrt(hr)+sqrt(hl));
cav=sqrt(g*(hr+hl)/2);
if k==1
  ans=dh/2-(duh-uav*dh)/2/cav;
  return
elseif k==2
  ans=dh/2+(duh-uav*dh)/2/cav;
  return
end