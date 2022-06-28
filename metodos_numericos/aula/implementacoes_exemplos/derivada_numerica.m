clc
clear all
close all

% Derivação Numérica
f = @(x) x^2+log(x);

x0 = 2;
h = 0.0001;

dfn = (f(x0+h)-f(x0))/h;
disp('Derivada Numérica = ')
disp(dfn)
