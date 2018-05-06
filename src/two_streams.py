import numpy as np 
import matplotlib.pyplot as plt


N = {"horizontal":{"inputs":5,"hidden":{"layers":2,"neurons":3},"output":1},
	 "vertical":{"associative layer":2},"patterns":2}


#-- Initialize network
activation_function = lambda inpt: 150*max(np.tanh((inpt-bias)/150),0)
inputs = np.zeros((N["horizontal"]["inputs"],))
hidden_layers = np.zeros((N["horizontal"]["hidden"]['neurons'],N["horizontal"]['hidden']['layers']))
#A more flexible constructor would allow for differenct numbers of neurons in each hidden layer

output = np.zeros((N["horizontal"]['output']))
associative_layer = np.zeros((N["vertical"]['associative layer'],))

sparsity = 0.25

patterns_to_recognize = np.array([np.random.choice([0,1],size = hidden_layers.size,p=[1-sparsity,sparsity])
									for _ in range(N["patterns"])])


starting_input = patterns_to_recognize[0]
M = 1.25/((1-sparsity)*sparsity*hidden_layers.size)*np.sum([np.outer(pattern-sparsity*np.ones((pattern.shape)),pattern-sparsity*np.ones((pattern.shape)))
																for pattern in patterns_to_recognize],axis=-1)	

print (M)
M = np.divide(M,1./(sparsity*hidden_layers.size)*np.ones(M.shape))
W = np.linalg.pinv(patterns_to_recognize.T)
for _ in range(10): #Just a few time steps
	print ('Hidden Layer Activity. ',patterns_to_recognize[0,:])
	print ('Feedforwward Contribution of HLA. ', W.dot(patterns_to_recognize[0,:]))

	print (M.T.dot(associative_layer))

'''
print xinv.dot(patterns_to_recognize[1,:])

print M
#For now, hidden layers are perfect copy of input


fig = plt.figure()
'''
