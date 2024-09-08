# leetcode 649

# Dota2 Senate 

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_votes, d_votes = 0,0
        q = []
        for char in senate: 
            q.append(char)
            if char == 'D':
                d_votes += 1 
            else:
                r_votes += 1 
        r_stop, d_stop = 0, 0 

        while q:
            char = q.pop(0) 
            if char == 'D':
                if d_stop == 0: 
                    if d_votes == len(q)+1: 
                        return 'Dire'
                    else: 
                        r_votes -= 1
                        r_stop += 1
                        q.append('D')
                else:
                    d_stop -= 1 
            else:
                if r_stop == 0: 
                    if r_votes == len(q)+1: 
                        return 'Radiant'
                    else: 
                        d_votes -= 1
                        d_stop += 1 
                        q.append('R')
                else:
                    r_stop -= 1 


senate = "RRDDDDDDDRRDRRDDRRRR"
test = Solution().predictPartyVictory(senate)
print(test)

# O(N) time amd space complexeity. 


'''
Method: 
2 queues or single queue approach
single queue
1. have vote counters for d and r
2. have stop counters for skips
3. convert string to list of characters and get the vote counts. 
4. while q - pop and check the character
5. if == D, check d stops 
6. if d_stops == 0: check to see if the d_votes = len(q) + 1, if so then 'Dire'
7. else reduce the r voles, increase the r stops and append D
8. for the R case do the opposite to the d steps. 

two queue case
1. iterate through the list and add the indexes to the appropriate R or D queue
2. while loop for the queues
3. pop from both queues
4. check which has the smaller index (higher priority)
5. that element is appended to the respective queue while the other is not. 
6. continue until 1 or both queues are empty
7. return criteria check which queue has data left in it. 
'''

from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()
        for i, char in enumerate(senate): 
            if char == 'D': 
                D.append(i)
            else: 
                R.append(i)
        
            
        while D and R: 
            d = D.popleft()
            r = R.popleft()

            if r < d: 
                R.append(r+len(senate))
            else: 
                D.append(d+len(senate))

        return 'Radiant' if R else 'Dire' 
        

senate = "DRRDRDRDRDDRDRDR"
test = Solution().predictPartyVictory(senate)
print(test)


# O(N) time amd space complexeity. 