def SymbolArray(Genome, symbol):
    # type your code here
    symbolArray = {}
    genomeLen = len(Genome)
    extendedGenome = Genome + Genome[0:genomeLen//2]
    for i in range(0, genomeLen):
        symbolArray[i] = PatternCount(extendedGenome[i:i+genomeLen//2], symbol)
    return symbolArray
