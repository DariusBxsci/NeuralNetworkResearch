def prefix(op, num1, num2):
  if op == "+":
    return num1 + num2
  elif op == "-":
    return num1 - num2
  else:
    # handle invalid op
    return 

def evalPrefix(input): #takes array of inputs in prefix notation
    if len(input) == 1:
        return input[0]
    else:
        subin = input[(len(input)-1)/2 - 1 : (len(input)-1)/2 + 2]
        print subin
        ret = input[0:(len(input)-1)/2 - 1] + [prefix(subin[0],int(subin[1]),int(subin[2]))] + input[(len(input)-1)/2 + 2:len(input)]
        return evalPrefix(ret)

def evaluateNeuron(input):
    ops = [None] * len(input);
    for i in input:
        ops[i[1]] = i[0]
    return evalPrefix(ops)

print evaluateNeuron([['4',2],['2',4],['3',3],['+',0],['-',1]])
