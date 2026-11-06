import numpy as np

#Derivada centrada
def df(x,f, h =0.001): 
    return (f(x+h)-f(x-h))/(2*h)
