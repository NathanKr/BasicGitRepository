function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad


% X 12x2 , all ready with x0=1
% y 12x1
% theta 2x1  theta0 , theta1
% lambda 1x1

m = length(y); % number of training examples

% You need to return the following variables correctly 
%J = 0;


h = X * theta; % 12x2 * 2x1 --> 12x1
e_vec = h - y; %12x1
Je = (1/2/m)*(e_vec' * e_vec);
ThetaWithoutBias = theta(2:size(theta));
Jreg = (lambda/2/m)*(ThetaWithoutBias'*ThetaWithoutBias);
J = Je + Jreg;



grad =  (1/m)*X' *e_vec;
grad(2:end) = grad(2:end)+(lambda/m)*theta(2:end);


size(grad)

end
