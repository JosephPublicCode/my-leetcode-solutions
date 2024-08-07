# leetcode 155

# Min Stack 

class MinStack():
    def __init__(self):
        self.data = []
        self.min = []

    def push(self, val:int) -> None: 
        self.data.append(val)
        if len(self.min) == 0: 
            self.min.append(val)
        elif val <= self.min[-1]: 
            self.min.append(val)


    def pop(self) -> None: 
        if self.data[-1] == self.min[-1]:
            self.data.pop()
            self.min.pop()
        else:
            self.data.pop()


    def top(self) -> int: 
        if len(self.min) == 0:
            return
        else:
            return self.data[-1]
    
    def getMin(self):
        if len(self.min) == 0:
            return 
        else:
            return self.min[-1]
        

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
print(minStack.top() )
print(minStack.getMin())


'''
Operation Time & Space Complexeities:

additional space complexeity: O(N) additional space. 

Time
Push: O(1)
Pop: O(1)
Top: O(1)
getMin: O(1)
'''        


'''
Method: 

1. initialize two data structures: data and min 
2. append to the data, append to min if value is less than or equal to top. 
3. pop from both if top of min and data is the same, otherwise pop from data only. 
4. top look at the top of the stack. 
5. getMin return top of min stack. 

'''



class MinStackAlt():
    def __init__(self):
        self.data = []
        self.min = []

    def push(self, val:int) -> None: 
        self.data.append(val)
        if self.min is None: 
            self.min.append(val)
        elif val <= self.min[-1]: 
            self.min.append(val)
        elif val > self.min[-1]:
            self.min.append(self.min[-1])


    def pop(self) -> None: 
        self.data.pop()
        self.min.pop()


    def top(self) -> int: 
        return self.data[-1]
    
    def getMin(self):
        return self.min[-1]
    
    def pushAlt(self,val:int) -> None:
        self.stack.append(val)
        val = min(val,self.min[-1] if self.min else val)
        self.min.append(val)