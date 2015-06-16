function [teta, J_history] = gradientDescentMulti(X, y, teta, alfa, num_iters)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

%X :           m x 3 (first coulmn is 1)
% y :           m x 1
% teta :   3 x 1 
% num_iters :           1x1


% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);


for i = 1:num_iters

        % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    h=X*teta;
    teta(1) = teta(1) - (alfa/m)*sum(h - y) ;
    teta(2) = teta(2) - (alfa/m)*(h - y)'*X(:,2) ;
    teta(3) = teta(3) - (alfa/m)*(h - y)'*X(:,3) ;

    % Save the cost J in every iteration    
    J_history(i) = computeCost(X, y, teta);

end

end
