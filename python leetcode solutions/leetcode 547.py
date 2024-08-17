# leetcode 547

# number of provinces


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        counter = 0 
        visit = set()

        def dfs(i:int):
            if i in visit: 
                return
            visit.add(i)

            for j, val in enumerate(isConnected[i]):
                if i != j and val == 1 and j not in visit:
                    dfs(j)


        for i in range(len(isConnected[0])): 
            if i not in visit: 
                counter += 1 
                dfs(i)

        return counter


isConnected = [[1,1,0],[1,1,1],[0,1,1]]

test = Solution().findCircleNum(isConnected)
print(test)

# Time Complexeity: O(V(V+E))


'''
Method: 
helper dfs function on matrix
1. iterate through the matrix
2. increase counter and run dfs if not visited
3. dfs - enumerate the indexes and values to determine if dfs needs to be ran


'''