def addIntChar(x, y):
    return x + ord(y)

def checkIfE1ErrorIsPresent(inputStr):
    n = len(inputStr)
    
    if n <= 0:
        return True
        
    if not inputStr.isupper():
        return True
        
    if inputStr[0] == " " or inputStr[0] != "(":
        return True
    
    if inputStr[n-1] == " " or inputStr[n-1] != ")":
        return True
    
    for i in range(0, n, 6):
        if inputStr[i] == "(" and inputStr[i+1].isalpha() and inputStr[i+2] == "," and inputStr[i+3].isalpha() and inputStr[i+4] == ")":
            continue
        else:
            return True
    
    return False

def checkIfE2ErrorIsPresent(nodes, graph, node):
    for i in range(1, len(nodes), 6):
        parent = ord(nodes[i]) - ord('A')
        child = ord(nodes[i+2]) - ord('A')

        if graph[parent][child]:
            return True
        
        graph[parent][child] = True
        node.add(addIntChar(parent, 'A'))
    return False

def checkIfE3ErrorIsPresent(graph):
    for i in range(26):
        count = 0
        for j in range(26):
            if graph[i][j]:
                count += 1
        
        if count > 2:
            return True
    
    return False
    
def dfs(node, graph, visited):
    if visited[node - ord('A')]:
        return True
    
    visited[node - ord('A')] = True
    
    for i in range(26):
        if graph[node - ord('A')][i]:
            if dfs(addIntChar(i, 'A'), graph, visited):
                return True

    return False

def helper(root, graph):
    l, r = "", ""

    for i in range(26):
        if graph[root - ord('A')][i]:
            l = helper(addIntChar(i, 'A'), graph)
            for j in range(i+1, 26):
                if graph[root - ord('A')][j]:
                    r = helper(addIntChar(j, 'A'), graph)
                    break
            break
    
    return "(" + chr(root) + l + r + ")"


def processString(inputStr):
    E1 = checkIfE1ErrorIsPresent(inputStr)
    if E1:
        return "E1"
        
    graph = [[False for x in range(26)] for y in range(26)]
    node = set()
    
    E2 = checkIfE2ErrorIsPresent(inputStr, graph, node)
    E3 = checkIfE3ErrorIsPresent(graph)
    
    if E2:
        return "E2"
    elif E3:
        return "E3"
        
    numRoots, root = 0, " "
    
    for n in node:
        for i in range(26):
            if graph[i][n - ord('A')]:
                break
            
            if i == 25:
                numRoots += 1
                root = n
                
                visited = [False]*26
                if dfs(n, graph, visited):
                    return "E5"
    
    if numRoots == 0:
        return "E5"
    elif numRoots > 1:
        return "E4"
    
    return helper(root, graph)

def main():
    #inputStr = input()
    inputStr = "(A,B)i(A,C)"
    result = processString(inputStr)
    print(result)
    
main()