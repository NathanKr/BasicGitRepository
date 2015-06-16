function [J, grad] = costFunction(theta, X, y)
%COSTFUNCTION Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost
%   w.r.t. to the parameters.

%X :            m x 3 (first coulmn is 1)
% y :           m x 1
% teta :   3 x 1 
% num_iters :           1x1


% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 

h=sigmoid(X*theta);
e = -y.* log(h) - (1-y).*log (1 - h);
J =(1/m)*sum(e);

%grad = zeros(size(theta));

%grad(1) = (1/m)*sum( h- y);
%grad(2) = (1/m)*sum(( h- y).*X( :,2));
%grad(3) = (1/m)*sum(( h- y).*X( :,3));

grad = X'* (h - y) / m;

end
