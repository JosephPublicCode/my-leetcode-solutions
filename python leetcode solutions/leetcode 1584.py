# leetcode 1584

# Min Cost to Connect all Points
import heapq
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        
        n = len(points)

        adj = { i:[] for i in range(n)}

        for i in range(n): 
            x1, y1 = points[i]
            for j in range(i+1,n): 
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist,i])

        res = 0 
        visit = set() 
        min_heap = [[0,0]]
        while len(visit) < n: 
            weight, node = heapq.heappop(min_heap)
            if node in visit: 
                continue
            res += weight
            visit.add(node)
            for cost, neighbor in adj[neighbor]: 
                if neighbor not in visit: 
                    heapq.heappush(min_heap, [cost, neighbor]) 
        return res
    
# Time Complexeity: O(E log V)
# Space Complexeity: O(E + V)

'''
Method: 
manhatten distances followed by prims algorithm, 
see my prim notes for more details

'''


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        visited = set()
        q = [(0, 0)]

        edges = 0
        res = 0
        while edges < len(points):
            cost, node = heapq.heappop(q)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            edges += 1
            for i in range(len(points)):
                if i in visited:
                    continue
                dist = self.getDist(points[node], points[i])
                heapq.heappush(q, (dist, i))
        return res


    def getDist(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)