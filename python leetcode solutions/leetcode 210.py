# leetcode 210 

# Course Schedule II 
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        graph = defaultdict(list)
        for i in range(numCourses): 
            graph[i] = []

        for [c, p] in prerequisites: 
            graph[c].append(p) 

        S = []
        for key, value in graph.items(): 
            if value == []:
                S.append(key)
        
        res = []
        while S: 
            node = S.pop()
            res.append(node)
            for key, value in graph.items(): 
                if node in value: 
                    value.remove(node)
                    if value ==[]: 
                        S.append(key)
        
        return (res if len(res) == numCourses else [])


numCourses = 5
prerequisities = [['d','b'],['e','d'],['e','a'],['e','c']]
test = Solution().findOrder(numCourses,prerequisities)
print(test)

# Time Complexeity: 
# Space Complexeity: O(N+V)

'''
Method: see my leetcode 207 solution for more details

Topological sort algorithms following Kahn's Algorithm.
same as previous just append key values as you see them to a result list. 

Solution below: 
Similar to my dfs from leetcode 207

This solution could also be done with an orderedSet from the ordered_set module 
This would remove the need for a visit set and result array. 
'''

from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        graph = {i:[] for i in range(numCourses)}
        for c, p in prerequisites: 
            graph[c].append(p)

        res = []
        visit, cycle = set(), set()
        def dfs(c): 
            if c in cycle: 
                return False
            if c in visit: 
                return True
            
            cycle.add(c)
            for neighbor in graph[c]: 
                if dfs(neighbor) == False: 
                    return False
            cycle.remove(c)
            visit.add(c)
            res.append(c)
            return True
                
        for c in range(numCourses): 
            if dfs(c) == False: 
                return []
        return res

