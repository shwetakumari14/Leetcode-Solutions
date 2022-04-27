class MinStack:

    def __init__(self):
        self.stack = []        

    def push(self, val):
        currMin = self.getMin()
        if currMin == None or val < currMin:
            currMin = val
        self.stack.append((val, currMin))

    def pop(self):
        self.stack.pop()
        

    def top(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack)-1][0]
        

    def getMin(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack)-1][1]
        


obj = MinStack()
obj.push(10)
obj.push(5)
#obj.pop()
obj.push(2)
obj.push(12)
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3,  " ", param_4)