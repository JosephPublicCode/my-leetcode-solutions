# leetcode 933

# Number of Recent Calls
from collections import deque
class RecentCounter:

    def __init__(self):
        self.counter = deque()

    def ping(self, t: int) -> int:
        self.counter.append(t)
        while self.counter[0] < (t - 3000):
            self.counter.popleft()
        return len(self.counter)
    

obj = RecentCounter()
print(obj.ping(642),
obj.ping(1849),
obj.ping(4921),
obj.ping(5936),
obj.ping(5957))

# Time Complexeity: O(n)
# Space Complexeity: O(n)


'''
Method: 
1. append the time
2. while values with t-3000 exists 
3. popleft. 
'''

class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        if t:
            self.counter.append(t)
        while self.counter[0] < (t - 3000):
            self.counter.pop(0)
        return len(self.counter)

obj = RecentCounter()
print(obj.ping(642),
obj.ping(1849),
obj.ping(4921),
obj.ping(5936),
obj.ping(5957))