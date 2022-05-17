clc
clear all
close all

pkg load control
1
num =1;
den = [2 1];
H = tf(num, den)
bode(H)
