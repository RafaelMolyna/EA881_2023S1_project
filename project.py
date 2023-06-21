import numpy as np

msgFile = open('file_sent.txt', mode='r')
msgText = msgFile.read()

t1 = 'abc ABC 123'
dp = float(input('type the standard deviation: '))
numRep = 8

def codefy(str):
    # chat to int
    ascList = map(ord, str)
    
    # int to bin
    intToBinaryStr = lambda n: format(n, 'b').rjust(8, '0')
    binStrings = map(intToBinaryStr, ascList)

    # join bit strings
    binSequence = ''.join(binStrings)

    # [0,1] -> [-1,1]
    bitDict = {'0': -1, '1': 1}
    strToBit = lambda b: bitDict[b]

    bitList = list(map(strToBit, binSequence))

    return np.array(bitList)

def addNoise(codeList, dp):
    return codeList + np.random.normal(scale=dp, size=[len(codeList)])

def filter(w):
    return np.array(list(map(lambda bit: 1 if bit > 0 else 0, w)))

def decode(codeBin):
    # int chunks
    binSplited = np.split(codeBin, len(codeBin)/8)

    # to list of integers:
    binListToInt = lambda c: int(''.join(map(str, c)), base=2)
    intList = map(binListToInt, binSplited)

    # to char:
    decodedString = ''.join(map(chr, intList))
    
    return decodedString


msgInput = msgText

codeList = codefy(msgInput)

# codeNoised = addNoise(codeList, dp / numRep)

noise = np.zeros(len(codeList))
for rep in range(numRep):
    noise += np.random.normal(scale=dp, size=[len(codeList)])
noise /= numRep
codeNoised = codeList + noise

codeFiltered = filter(codeNoised)

msgOutput = decode(codeFiltered)

print(msgInput)
print(msgOutput)

# Errors:
errorStr = ''.join([('_' if x == y else 'X') for x, y in zip(msgInput, msgOutput)])
numErrors = errorStr.count('X')
porcErros = 100 * numErrors / len(msgInput)
numChannelUsage = len(codeList) * numRep

print(f'N° channel usage times: {numChannelUsage}')
print(f'N° erros: {numErrors}')
print(f'N° erros: {numErrors}')
print('Porc erros: {0:.2f} % '.format(porcErros))
print(numErrors)



