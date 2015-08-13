function [C, sigma] = dataset3Params(X, y, Xval, yval)
%EX6PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = EX6PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
%C = 1;
%sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%




% We set the tolerance and max_passes lower here so that the code will run
% faster. However, in practice, you will want to run the training to
% convergence.

C_vec = [0.01 0.03 0.1 0.3 1 3 10 30];
sigma_vec = [0.01 0.03 0.1 0.3 1 3 10 30];
error = realmax;

for i_C=1:length(C_vec)
    for i_sigma=1:length(sigma_vec);

    C_temp=    C_vec(i_C);
    sigma_temp = sigma_vec(i_sigma);
    model= svmTrain(X, y, C_temp, @(x1, x2) gaussianKernel(x1, x2, sigma_temp)); 
     pred = svmPredict(model, Xval);
     error_temp = mean(abs(pred - yval));

     if(error_temp < error)
         error = error_temp;
         C = C_temp;
         sigma = sigma_temp;
     end
     
     end
end




% =========================================================================

end