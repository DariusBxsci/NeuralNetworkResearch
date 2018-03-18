import numpy as np
from random import *

def generate_training_data():
    
    input_examples = []
    output_examples = []

    for i in range(1000): #generate based on random combinations of symptoms
        iarr = [0,0,0,0,0,0,0]
        oarr = [False]
        num_symptoms = 0;
        all_even = True;
        all_odd = True;
        for x in range(7):
            if (int(random() * 100) % 2 == 0):
                iarr[x] = 1
                num_symptoms += 1
                
                if(x % 2 == 0 and all_odd):
                    all_odd = False
                if(x % 2 == 1 and all_even):
                    all_even = False

        if (all_even or all_odd):
            i -= 1
            continue
        elif (int(random() * 100) >= num_symptoms * 10):
            oarr[0] = True

        input_examples.append(iarr)
        output_examples.append(oarr)

    for i in range(250):
        iarr = [0,0,0,0,0,0,0]
        oarr = [0]
        for x in range(7):
            if (int(random() * 100) % 2 == 0 and x % 2 == 0):
                iarr[x] = 1
        
        if (int(random() * 100) >= 5):
            oarr[0] = True
        
        input_examples.append(iarr)
        output_examples.append(oarr)

    for i in range(250):
        iarr = [0,0,0,0,0,0,0]
        oarr = [0]
        for x in range(7):
            if (int(random() * 100) % 2 == 0 and x % 2 == 1):
                iarr[x] = 1
        
        if (int(random() * 100) >= 95):
            oarr[0] = True
        
        input_examples.append(iarr)
        output_examples.append(oarr)
  
    #print input_examples

    input_examples = np.array(input_examples)
    output_examples = np.array(output_examples)

    #print input_examples.shape

    return (input_examples,output_examples)




