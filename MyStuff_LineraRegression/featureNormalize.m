function [X_norm, avg, sigma] = featureNormalize(X)
%FEATURENORMALIZE Normalizes the features in X 
%   FEATURENORMALIZE(X) returns a normalized version of X where
%   the mean value of each feature is 0 and the standard deviation
%   is 1. This is often a good preprocessing step to do when
%   working with learning algorithms.



%         First, for each feature dimension, compute the mean
%               of the feature and subtract it from the dataset,
%               storing the mean value in mu. Next, compute the 
%               standard deviation of each feature and divide
%               each feature by it's standard deviation, storing
%               the standard deviation in sigma. 
%
%               Note that X is a matrix where each column is a 
%               feature and each row is an example. You need 
%               to perform the normalization separately for 
%               each feature. 
%


avg = mean(X);
sigma = std(X);

x1 = X(:,1) ;% no need to change its all one
x2 = (X(:,2) - avg(2)) / sigma(2);
x3 = (X(:,3) - avg(3)) / sigma(3);
X_norm = [x1 x2 x3];





% ============================================================

end
