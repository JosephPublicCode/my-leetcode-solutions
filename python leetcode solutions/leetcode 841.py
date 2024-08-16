# leetcode 841

# Keys and Rooms 

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        room_number = len(rooms)
        visit = set()

        def dfs(i): 
            if i in visit: 
                return None
            visit.add(i)

            for key in rooms[i]: 
                dfs(key)

        
        dfs(0)
        return len(visit) == room_number
    
rooms = [[1,3],[3,0,1],[2],[0]]
# [[1],[2],[3],[]]
test = Solution().canVisitAllRooms(rooms)
print(test)

# Time Complexeity: O(n)
# Space complexeity: O(n)

'''
Method: 
recursive DFS algorithm.
1. attempt to visit all nodes
2. recursive dfs on all keys at the given node. 
3. check if the length of the visit set == number of rooms. 
'''
