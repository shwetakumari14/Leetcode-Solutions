def parseInputs(inputStr, adjList, numParents, root):
    parent, index, E5Error = "", 0, False

    for i in range(len(inputStr)):
        if inputStr[i] != '(' and inputStr[i] != ')' and inputStr[i] != ',' and inputStr[i] != ' ':
            index += 1
            if index % 2 == 1:
                if i - 1 >= 0 and inputStr[i-1] != '(':
                    print("E1")
                    return False
                elif i + 1 < len(inputStr) and inputStr[i+1] != ',':
                    print("E1")
                    return False
                
                parent = inputStr[i]
            else:

                if i - 1 >= 0 and inputStr[i-1] != ',':
                    print("E1")
                    return False
                elif i + 1 < len(inputStr) and inputStr[i+1] != ')':
                    print("E1")
                    return False
                for j in range(len(adjList[parent])):
                    if adjList[parent][j] == inputStr[i]:
                        print("E2")
                        return False
                
                if len(adjList[parent]) == 2: 
                    print("E3")
                    return False
                
                numParents[inputStr[i]] += 1
                numParents[parent]
                if numParents[inputStr[i]] == 2:
                    E5Error = True
                
                adjList[parent].append((inputStr[i]))
                index = 0
        else:
            if i - 1 <= 0 and inputStr[i] == ' ':
                if inputStr[i] == ' ': 
                    print("E1")
                    return False
    
    numRoots = 0
    for key, value in numParents.items():
        if value == 0:
            root = key
            numRoots += 1
            if numRoots == 2: 
                print("E4")
                return False

    
    if E5Error == True:
        print("E5")
        return False
    
    return True


def printlexiSExpression(adjList, current):
    
    print("(",current)
    numChild = len(adjList[current])
    if numChild == 1:
          printlexiSExpression(adjList, adjList[current][0])
    elif numChild == 2:
        if adjList[current][0] < adjList[current][1]: 
              printlexiSExpression(adjList, adjList[current][0])
              printlexiSExpression(adjList, adjList[current][1])
        else:
              printlexiSExpression(adjList, adjList[current][1])
              printlexiSExpression(adjList, adjList[current][0])

    print(")")

def main():
    inputStr = "(A,B) (A,C) (B,D) (D,C)"

    root = ""
    adjList, numParents = {}, {}

    if parseInputs(inputStr, adjList, numParents, root) == False:
        return
    
    printlexiSExpression(adjList, root)

main()