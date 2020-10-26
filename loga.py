import numpy as np
import random

def sigmoid(x, Θ_1, Θ_2):                                                        
    z = (Θ_1*x + Θ_2).astype("float")                                              
    return 1.0 / (1.0 + np.exp(-z)) 

def log_likelihood(x, y, Θ_1, Θ_2):                                                                
    sigmoid_probs = sigmoid(x, Θ_1, Θ_2)                                        
    return np.sum(y * np.log(sigmoid_probs) + (1 - y) * np.log(1 - sigmoid_probs))  

def gradient(x, y, Θ_1, Θ_2):                                                         
    sigmoid_probs = sigmoid(x, Θ_1, Θ_2)                                        
    return np.array([[np.sum((y - sigmoid_probs) * x),                          
                     np.sum((y - sigmoid_probs) * 1)]])                         

def hessian(x, y, Θ_1, Θ_2):                                                          
    sigmoid_probs = sigmoid(x, Θ_1, Θ_2)                                        
    d1 = np.sum((sigmoid_probs * (1 - sigmoid_probs)) * x * x)                  
    d2 = np.sum((sigmoid_probs * (1 - sigmoid_probs)) * x * 1)                  
    d3 = np.sum((sigmoid_probs * (1 - sigmoid_probs)) * 1 * 1)                  
    H = np.array([[d1, d2],[d2, d3]])                                           
    return H

def newtons_method(x, y):                                                             

                                                                     
    Θ_1 = 1                                                                     
    Θ_2 = 1                                                            
    Δl = np.Infinity                                                                
    l = log_likelihood(x, y, Θ_1, Θ_2)                                                                 
                                                      
    δ = .01                                                                 
    max_iterations = 15                                                           
    i = 0                                                                           
    while abs(Δl) > δ and i < max_iterations:                                       
        i += 1                                                                      
        g = gradient(x, y, Θ_1, Θ_2)                                                      
        hess = hessian(x, y, Θ_1, Θ_2)                                                 
        H_inv = np.linalg.inv(hess)                                                 
        # @ is syntactic sugar for np.dot(H_inv, g.T)¹
        Δ = H_inv @ g.T                                                             
        ΔΘ_1 = Δ[0][0]                                                              
        ΔΘ_2 = Δ[1][0]                                                              
                                                                                                                              
        Θ_1 += ΔΘ_1                                                                 
        Θ_2 += ΔΘ_2                                                                 
                               
        l_new = log_likelihood(x, y, Θ_1, Θ_2)                                                      
        Δl = l - l_new                                                           
        l = l_new                                                                
    return np.array([Θ_1, Θ_2])     

x1 = []
x2 = []
random.seed(1)
for x in range(40):
   
   x1 = np.append(x1,random.randint(1,69) + random.random())
   x2 = np.append(x2,random.randint(70,100) + random.random())

#x1 = x1.T
#x2 = x2.T
print(x1)
print(x2)
np.seterr(all='ignore')

print(newtons_method(x1,x2))


