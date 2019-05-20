
def PatternCount(Text, Pattern):
    # fill in your function here
    count = 0
    len_pattern = len(Pattern)
    iter_till_index = len(Text) - len_pattern + 1
    
    for i in range(iter_till_index):
        if(Text[i:i+len_pattern] == Pattern):
            count = count + 1
    return count

def FrequentWords(Text, k):
    # your code here
    frequencyMap = FrequencyMap(Text, k)
    mostOccurance = max(frequencyMap.values())
    frequentWordsList = []
    for key, value in frequencyMap.items():
        if (value == mostOccurance):
            frequentWordsList.append(key)
       
    return frequentWordsList

# Insert your completed FrequencyMap() function here.
def FrequencyMap(Text, k):
    # your code here
    frequencyMap = {}
    numOfWindowSlides = len(Text) - k + 1
    for i in range(numOfWindowSlides):
        if not Text[i:i+k] in frequencyMap:
            frequencyMap[Text[i:i+k]] = PatternCount(Text,Text[i:i+k])
    
    return frequencyMap


def ReverseComplement(Pattern):   
    # your code here
    ReversePattern = Reverse(Pattern)
    return Complement(ReversePattern)

# Copy your Reverse() function here.
def Reverse(Pattern):
    # your code here
    reversePattern = ""
    for char in Pattern:
        reversePattern = char+reversePattern
    return reversePattern   

# Copy your Complement() function here.
def Complement(Pattern):
    # your code here
    complementPattern = ""
    for char in Pattern:
        if(char=="A"):
            complementPattern = complementPattern+"T"
        elif(char=="T"):
            complementPattern = complementPattern+"A"
        elif(char=="G"):
            complementPattern = complementPattern+"C"
        elif(char=="C"):
            complementPattern = complementPattern+"G"
    return complementPattern

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    # your code here
    for i in range(len(Genome) - len(Pattern) + 1):
        if(Genome[i:i+len(Pattern)] == Pattern):
            positions.append(i)
    return positions
