function p = predictOneVsAll(all_theta, X)
%PREDICT Predict the label for a trained one-vs-all classifier. The labels 
%are in the range 1..K, where K = size(all_theta, 1). 
%  p = PREDICTONEVSALL(all_theta, X) will return a vector of predictions
%  for each example in the matrix X. Note that X contains the examples in
%  rows. all_theta is a matrix where the i-th row is a trained logistic
%  regression theta vector for the i-th class. You should set p to a vector
%  of values from 1..K (e.g., p = [1; 3; 1; 2] predicts classes 1, 3, 1, 2
%  for 4 examples) 

m = size(X, 1);

num_classes = size(all_theta, 1);
prob_ar=zeros(num_classes,1);

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);

% Add ones to the X data matrix
X = [ones(m, 1) X];




%loop all classes and get the one with max probability

 for i_m =1:m
    
     for i_num_classes=1:num_classes
         theta = all_theta(i_num_classes,:);
        Xi=X(i_m,:);

         prob_ar(i_num_classes) =   sigmoid( Xi*theta');
     end
     [~,i_max] = max(prob_ar);
     
     p(i_m) = i_max;
     
 end

% =========================================================================


end
