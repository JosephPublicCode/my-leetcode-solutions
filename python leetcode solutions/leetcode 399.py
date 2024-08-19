# leetcode 399

# Evaluate Division


from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:

        adj_list = defaultdict(list)
        for i, eqn in enumerate(equations): 
            u, v = eqn[0], eqn[1]
            w = values[i]
            adj_list[u].append((v,w))
            adj_list[v].append((u,1/w))
            
        
        def dfs(start, end,value, visit): 
            if start == end: 
                return value
            visit.add(start)

            for nei,weight in adj_list[start]: 
                if nei not in visit: 
                    nei_value =  dfs(nei,end,weight*value, visit)
                    if nei_value != -1: 
                        return nei_value

            return -1

        res = [] 
        for query in queries: 
            if query[0] not in adj_list \
                     or query[1] not in adj_list: 
                res.append(-1)

            else: 
                res.append(dfs(query[0],query[1],1,set()))
        return res



equations = [["a","b"],["b","c"]]
values = [2.0, 3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

# equations = [["a","b"],["b","c"],["bc","cd"]]
# values = [1.5,2.5,5.0]
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

test = Solution().calcEquation(equations,values,queries)
print(test)

# Time Complexeity: O(N(E+V))
# Space Complexeity: O(E+V)

'''
Method: 
Adjacency list formation of a weighted graph
dfs or bfs- time and space is the same for both cases. 
1. create adjacency list using defaultdict with weight and neighbors
2. create dfs helper function
3. iterate through the array - check if target and start are in the list
4. if in graph run and append the result. 

'''



# BFS approach 
class Solution: 
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        adj_list = defaultdict(list)
        for i, eqn in enumerate(equations): 
            u, v = eqn
            adj_list[u].append([v, values[i]])
            adj_list[v].append([u,1/values[i]])

        def bfs(src,target):
            if src not in adj_list or target not in adj_list: 
                return -1
            
            q, visit = deque(), set()
            q.append([src,1])
            visit.add(src)
            while q: 
                node, weight = q.popleft()
                if node == target: 
                    return weight
                for nei, wei in adj_list[node]: 
                    if nei not in visit: 
                        visit.add(nei)
                        q.append([nei,wei*weight])

            return -1 



        res =  [bfs(query[0],query[1]) for query in queries]
        return res
            
equations = [["a","b"],["b","c"]]
values = [2.0, 3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

test = Solution().calcEquation(equations,values,queries)
print(test)