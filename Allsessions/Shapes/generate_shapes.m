%% 
clear
clc
%%
addpath("/Users/verra/Documents/PhD/phd_task/Titration/Shapes/shapesPROA")

% we will need 100 x condition (+ colours!!) 

rho = 0.005; %0.01; %staircase result 
cs_plus = 0.5; % central cs + 
%n_gs = 5 %number of gs stimuli x side
%gs_last = cs_plus+(rho*n_gs)
%gs_first = cs_plus - (rho*n_gs)
%z = gs_first: rho:gs_last
z = 0.01:0.005:1

%%
ns = [5] %spikes
colors_rgb = [142   152   255; 0   198   255; 0   206   195; 122   189    51; 255   140    62; 255    95   192; 0 0 0]/255

for i = 1: length(ns)
    for r=1:length(z)
        ii = ns(i)
        rr = z(r)
        gen_shape(rr, ii, 12.5,colors_rgb(7,:) )
        
        fname = sprintf('F%d_S%d.png', r,ii);
        set(gcf, 'InvertHardCopy', 'off'); 
        set(gcf, 'PaperPosition', [0 0 10 10],'Color',[211/255 211/255 211/255]);
        
        saveas(gcf,sprintf('F%d_S%d.png', r,22))
        if r == 50
           savefig(sprintf('F%d_S%d.fig', r, 22))
        end
            
    end 
end

close all
