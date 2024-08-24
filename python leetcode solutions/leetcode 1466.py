# leetcode 1466 

# Reorder Routes to make all paths lead to the city zero

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        
        edges = {(u,v) for u,v in connections}
        neigh = {i:[] for i in range(n)}
        visit = set()
        count = 0 

        for u, v in connections: 
            neigh[u].append(v)
            neigh[v].append(u)
        
        def dfs(city): 
            nonlocal edges, neigh, visit, count
            
            for nei in neigh[city]: 
                if nei in visit: 
                    continue

                if (nei,city) not in edges: 
                    count +=1 
                visit.add(nei)
                dfs(nei)
        
        visit.add(0)
        dfs(0)
        return count
    
# Time Complexeity: O(n)
# Space Complexeity: O(n)

'''
Method:
recursive dfs
to do this assume that the graph is undirected and 
then iterate through the graphs from the 0. 
check if the graph correct direction is in the edges list
1. create the adjacency list with undirected edges and 
convert list of lists to dict of tuples for O(1) lookup. 
2. create a helper dfs function
3. grab the nonlocal functions. 
4. iterate through the neighbors. 
5. if visited then pass. 
6. check if the nei, city in the edges, if not then increase the counter
7. add to the visit set and run dfs on the nei. 
8. add 0 to visit and run dfs(0) then return the count. 
'''

       
       
       