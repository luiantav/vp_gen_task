% Adapted from Norbury paper - https://osf.io/2truz

%function to create scrambled image mask for use with perceptual
%discrimination tasks.

addpath("/Users/verra/Documents/PhD/phd_task/Titration/Shapes/shapes_png")


colors_rgb = [142   152   255; 0   198   255; 0   206   195; 122   189    51; 255   140    62; 255    95   192]/255
%conditions = [3,4,5,6,9,12]
conditions = [5,5,5,5,5,5]

for i = 1: length(conditions)
    s = conditions(i)
    
    img = imread(sprintf('F50_S%d.png', s)); %read in average image to scramble (e.g. rho=0.5 shape for discrim_test_delayed task)
    resize_f = round((size(img,1)/10))*10
    img = imresize(img,[resize_f NaN]);


    blockSize = 10;

    nRows = size(img, 1) / blockSize;
    nCols = size(img, 2) / blockSize;

    scramble = mat2cell(img, ones(1, nRows) * blockSize, ones(1, nCols) * blockSize, size(img, 3));
    scramble = cell2mat(reshape(scramble(randperm(nRows * nCols)), nRows, nCols));

    imshow(scramble);
    set(gcf, 'InvertHardCopy', 'off'); 
    set(gcf, 'PaperPosition', [0 0 10 10],'Color',[211/255 211/255 211/255]);
    saveas(gcf,sprintf('scramble_S%d.png', s))
end
close all