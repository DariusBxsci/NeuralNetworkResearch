import random


NUM_INPUTS = input("How many input neurons?")
NUM_PATTERNS = 2**2**NUM_INPUTS
NUM_TEST = 50
output_patterns = []

#create and generate output for a random perceptron
def process_random_perceptron(input):
	weights = []
	i = 0
	out = 0
	while i < NUM_INPUTS:
		weights.append(random.randint(-1000,1000)/500.0)
		i++
	i = 0
	while i < len(weights):
		out += weights[i]*input[i]
		i++
	return out

#generate random perceptrons and see if they correspond with a given output pattern
def validate_output_pattern(pat):
