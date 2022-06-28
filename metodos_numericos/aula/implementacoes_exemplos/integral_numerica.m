clc
clear all
close all

% Integral Numérica pelo Método dos Trapézios Repetidos
f = @(x) log(x);

a = 1;
b = 2;
n = 5;
h = (b - a)/n;

x = a:h:b; % De A até B pulando de h em h

y = f(x);
y_inter = y(2:end-1); % pode ser: y(2:n) -> vetor em matlab começa em 1
sum_y_inter = sum(y_inter);

Itr = (h/2)*(y(1)+2*sum_y_inter+y(n+1))
