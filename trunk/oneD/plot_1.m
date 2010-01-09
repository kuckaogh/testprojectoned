function plot_1(illustrate,sc,t,courant,x,y1,y2,plot_style,caption_position)

switch illustrate
    case(1)
        label_y = ' h '; 
        plot(x,y1,plot_style);
        xlabel(['x', '   Courant =',num2str(courant)]);
        ylabel([label_y,' : t = ',num2str(t),'s']);
        legend('Exact',sc,caption_position);
    case(2)
        label_y = ' u '; 
        plot(x,y2,plot_style);
        xlabel(['x', '   Courant =',num2str(courant)]);
        ylabel([label_y,' : t = ',num2str(t),'s']);
        legend('Exact',sc,caption_position);
    otherwise
end

