function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the
%   cost of using theta as the parameter for linear regression to fit the
%   data points in X and y. Returns the cost in J and the gradient in grad
 
% Initialize some useful values
m = length(y); % number of training examples
 
% You need to return the following variables correctly
J = 0;
grad = zeros(size(theta));
 
size(theta)
 


h = X * theta; % 12x2 * 2x1 --> 12x1
e_vec = h - y; %12x1
Je = (1/2/m)*(e_vec' * e_vec);
ThetaWithoutBias = theta(2:size(theta));
Jreg = (lambda/2/m)*(ThetaWithoutBias'*ThetaWithoutBias);
J = Je + Jreg;

 
% Gradient terms
% Notice how we use full vectorization here
% The trick is to compute the summatory term within the gradient function
% using a multiplication of the transpose of the input examples and
% the errors in our predictions. The transpose of X gives us all the feature
% i for all the examples in the i row and so on ...
% Also, since we DO NOT apply regularization for theta1, we use set the
% first element of a copy of theta as 0

% good grad     = ((X' * e_vec) / m) + ((lambda/m) * [0; theta(2:end)]);
%grad     = ((X' * (pred - y)) / m) + ((lambda/m) * [0; theta(2:end)]);

 
grad =  (1/m)*X' * e_vec;
grad(2:end) = grad(2:end)+(lambda/m)*theta(2:end);


end