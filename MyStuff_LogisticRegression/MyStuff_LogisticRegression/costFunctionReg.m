function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTION Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost
%   w.r.t. to the parameters.

%X :            m x 28 (first coulmn is 1)
% y :           m x 1
% teta :   28 x 1 
% num_iters :           1x1


% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 

h=sigmoid(X*theta);
e = -y.* log(h) - (1-y).*log (1 - h);
thetaForLambda =  theta(2:length(theta));
lambdaSum = (lambda/2/m)*(thetaForLambda'*thetaForLambda);
J =(1/m)*sum(e) + lambdaSum;

%grad = zeros(size(theta));

grad = X'* (h - y) / m + (lambda / m)*theta;
grad (1) = grad (1) -(lambda / m)*theta(1);

end