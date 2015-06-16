function [prob] = probability( theta , Xi )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
prob = sigmoid( Xi*theta );

end

