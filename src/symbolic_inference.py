
#code to demonstrate the capacity for neural networks to make symbolic inference
#In this example, a series of logical relationships are stated and used to train a neural network
#The goal is for the network to return a value close to 0 when asked if "mortal -> socrates"

#each tuple describes a situation where the first element implies the second, and the third
# gives the implication's truth value
predicates = [ ("socrates","human",1),
               ("human","mortal",1),
               ("socrates","mortal",1),
               ("mortal","human",0),
               ("human","socrates",0) ]
#The trained net should give ("socrates","mortal",0)

#encode the strings as 1-hot vectors
def encode_word(s):
    if s == "socrates":
        return (1,0,0)
    elif s == "human":
        return (0,1,0)
    else:
        return (0,0,1)
for i in predicates:
    x = encode_word(i[0])
    y = encode_word(i[1])
    i = (x,y,i[2])

import numpy as np

hidden_weights = np.random.randint(-3,3, size=(3,6,6))
output_weights = np.random.randint(-3,3, size=(6,1))

def run_network(i):
    i = i[0]+i[1]
    for mat in hidden_weights:
        i = np.matmul(i,mat)
        #print(i)
    return np.matmul(i,output_weights)

#example forward-pass
print(run_network(((0,0,1),(1,0,0))))


