function [all_theta] = oneVsAll(X, y, num_classes, lambda)
%ONEVSALL trains multiple logistic regression classifiers and returns all
%the classifiers in a matrix all_theta, where the i-th row of all_theta 
%corresponds to the classifier for label i
%   [all_theta] = ONEVSALL(X, y, num_classes, lambda) trains num_classes
%   logisitc regression classifiers and returns each of these classifiers
%   in a matrix all_theta, where the i-th row of all_theta corresponds 
%   to the classifier for label i

% y : 5000x1 each row corresponds to a digit
% X : 5000x400 (each raw is bitmap)

% Some useful variables
m = size(X, 1);
n = size(X, 2);

% You need to return the following variables correctly 
all_theta = zeros(num_classes, n + 1);

% Add ones to the X data matrix
X = [ones(m, 1) X];


%       fmincg works similarly to fminunc, but is more efficient when we
%       are dealing with large number of parameters.
%


    initial_theta = zeros(n + 1, 1);
    
    % Set options
    options = optimset('GradObj', 'on', 'MaxIter', 50);

    for i=1:num_classes  
    
         [all_theta(i,:)] = ...
        fmincg (@(t)(lrCostFunction(t, X, (y == i), lambda)), ...
                initial_theta, options);
    
    end

    
   


end
