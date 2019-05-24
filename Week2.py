def SymbolArray(Genome, symbol):
    # type your code here
    symbolArray = {}
    genomeLen = len(Genome)
    extendedGenome = Genome + Genome[0:genomeLen//2]
    for i in range(0, genomeLen):
        symbolArray[i] = PatternCount(extendedGenome[i:i+genomeLen//2], symbol)
    return symbolArray

def FasterSymbolArray(Genome, symbol):
    array = {}
    # your code here
    genomeLen = len(Genome)
    extendedGenome = Genome + Genome[0:genomeLen//2]
    initialCount = PatternCount(extendedGenome[0:genomeLen//2], symbol)
    array[0] = initialCount
    for i in range(1, genomeLen):
        if(extendedGenome[i-1] == symbol):
            if(extendedGenome[i+genomeLen//2-1] == symbol):
                array[i] = array[i-1]
            else:
                array[i] = array[i-1] - 1
        else:
            if(extendedGenome[i+genomeLen//2-1] == symbol):
                array[i] = array[i-1] + 1
            else:
                array[i] = array[i-1]
            
    return array
