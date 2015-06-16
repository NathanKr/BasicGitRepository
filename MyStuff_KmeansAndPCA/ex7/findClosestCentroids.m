function idx = findClosestCentroids(X, centroids)
%FINDCLOSESTCENTROIDS computes the centroid memberships for every example
%   idx = FINDCLOSESTCENTROIDS (X, centroids) returns the closest centroids
%   in idx for a dataset X where each row is a single example. idx = m x 1 
%   vector of centroid assignments (i.e. each entry in range [1..K])
%

% Set K
K = size(centroids, 1);

% You need to return the following variables correctly.
m=size(X,1);
idx = zeros(m, 1);



% ====================== YOUR CODE HERE ======================
% Instructions: Go over every example, find its closest centroid, and store
%               the index inside idx at the appropriate location.
%               Concretely, idx(i) should contain the index of the centroid
%               closest to example i. Hence, it should be a value in the 
%               range 1..K
%
% Note: You can use a for-loop over the examples to compute this.
%

for i_m=1:m
    min_ditance=realmax;
    i_k_centeroid_min_ditance=0;
    x_i_m = X(i_m,:);
    
    for i_k = 1:K
        center = centroids(i_k,:);
        distance = norm(center-x_i_m);
        if(distance < min_ditance)
            i_k_centeroid_min_ditance = i_k;
            min_ditance = distance;
        end
    end
    
    idx(i_m) = i_k_centeroid_min_ditance;
end





% =============================================================

end

