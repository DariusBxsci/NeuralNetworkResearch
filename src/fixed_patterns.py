import numpy as np 
import matplotlib.pyplot as plt

#To get started choose only a few patterns to make the matrix intertible

N = {"horizontal":{"inputs":5,"hidden":{"layers":2,"neurons":3},"output":1},
	 "vertical":{"associative layer":2},"patterns":2}


for _ in xrange(10):
	arr = np.array([np.random.choice([0,1],size=N['horizontal']['hidden']['neurons']*N['horizontal']['hidden']['layers'])
					for _ in xrange(N['horizontal']['hidden']['neurons']*N['horizontal']['hidden']['layers'])])

	if np.linalg.det(arr) != 0:
		#Should normalize array
		#arr = np.divide(arr,np.linalg.norm(arr))
		B = np.linalg.inv(arr)
		
		for i in xrange(arr.shape[0]):
			print '-----------------'
			print 'Presenting pattern %d'%i
			presentation = B.dot(arr[:,i])
			presentation[np.absolute(presentation)<0.0001] #HACK
			idx = np.where(presentation==1)[0]
			if idx:
				print idx[0] == i
			else:
				print 'Did not recognize pattern %d'%i
				print arr[:,i]
				print B.dot(arr[:,i])
	'''
	fig = plt.figure()
	ax = fig.add_subplot(111)
	cax = ax.imshow(arr, interpolation='nearest',aspect='auto', cmap=plt.cm.bone_r)
	plt.colorbar(cax)
	ax.set_xlabel('Pattern')
	ax.set_ylabel('Hidden Neuron')
	fig.tight_layout()
	plt.show()
	'''