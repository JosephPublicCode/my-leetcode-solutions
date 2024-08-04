# leetcode 207

# Course Scheduler
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        # convert to adjacency list 
        graph = defaultdict(list)
        for u,v in prerequisites: 
            graph[u].append(v)
            if v not in graph: 
                graph[v] = []

        # add all non dependants to a queue
        S = deque()
        counter = 0 
        for node in graph:
            if len(graph[node]) == 0: 
                S.append(node)
                counter +=1

        # continue until the queue is empty
        while S: 
            incoming = S.popleft()
            for node in graph: 
                if incoming in graph[node]: 
                    graph[node].remove(incoming)
                    if len(graph[node]) == 0: 
                        S.append(node)

        # check if all adjacency lists are empty
        for node in graph:
            if len(graph[node]) != 0: 
                return False
        return True

numCourses = 2
prerequisities = [[1,0],[0,1]]
test = Solution().canFinish(numCourses,prerequisities)
print(test)


#  Time O(V + E)
#  space O(V)

'''
This solution is based on Topological Sort - Kahn's Algorithm. 
https://en.wikipedia.org/wiki/Topological_sorting 

method: 
1. convert list of edges to adjacency lists
2. add non-dependent nodes to deque
3. pop from deque, remove node from all neighbor lists
4. append new non-dependent nodes to deque
5. check all nodes in graph to confirm no neighbors 

'''

# dfs alternative solution. 

class Solution: 
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        graph = defaultdict(list)
        # create an adjacency list
        for u,v in prerequisites: 
            graph[u].append(v)
            if v not in graph: 
                graph[v] = []
        

        visit = set() 
        # dfs helper function
        def dfs(node): 
            # base cases
            if node in visit: 
                return False
            if graph[node] == []: 
                return True
            
            # vist then dfs on neighbors
            visit.add(node)
            for neighbor in graph[node]: 
                if not dfs(neighbor): 
                    return False
            visit.remove(node)
            visit[node] = []
            return True
        
        # check all nodes in the graph
        for node in graph: 
            if not dfs(node): return False
        return True
