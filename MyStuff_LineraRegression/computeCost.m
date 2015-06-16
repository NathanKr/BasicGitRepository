function J = computeCost(X, y, teta)
%COMPUTECOST Compute cost for linear regression
%   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

%X :           m x 2 (first coulmn is 1)
% y :           m x 1
% teta :   2 x 1 
% J :           1x1



% Initialize some useful values
m = length(y); % number of training examples



h=X*teta;
e=h-y;
J = (2/m)*(e'*e);




end
