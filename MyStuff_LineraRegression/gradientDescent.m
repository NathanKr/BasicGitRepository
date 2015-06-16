function [teta, J_history] = gradientDescent(X, y, teta, alfa, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

%X :           m x 2 (first coulmn is 1)
% y :           m x 1
% teta :   2 x 1 
% num_iters :           1x1


% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);
x=X(:,2);

for i = 1:num_iters
    h=X*teta;
    teta(1) = teta(1) - (alfa/m)*sum(h - y) ;
    teta(2) = teta(2) - (alfa/m)*(h - y)'*x ;


    % Save the cost J in every iteration    
    J_history(i) = computeCost(X, y, teta);

end

end
