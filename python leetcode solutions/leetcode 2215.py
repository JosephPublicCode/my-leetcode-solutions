# leetcode 2215

# Find the Different of Two Arrays


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        res = [[],[]]
        set1 =  {_ for _ in nums1}
        set2 = {_ for _ in nums2}

        nums1 = [_ for _ in set1]
        nums2 = [_ for _ in set2]

        for i in nums1:
            if i not in set2: 
                res[0].append(i)


        for i in nums2: 
            if i not in set1: 
                res[1].append(i)
        return res
    
nums1 = [1,2,3]

nums2 = [2,4,6]

test = Solution().findDifference(nums1,nums2)
print(test)

# Time Complexeity: O(n+m)
# Space Complexeity: O(n+m)

# iterate through the sets

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        res = []
        set1 =  set(nums1)
        set2 = set(nums2)

        list1 = []
        list2 = []

        for i in set1:
            if i not in set2: 
                list1.append(i)


        for i in set2: 
            if i not in set1: 
                list2.append(i)
                
        res.append(list1)
        res.append(list2)
        return res


#  set operations

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        res = []
        set1 =  set(nums1)
        set2 = set(nums2)

        diff1 = set1.difference(set2)
        diff2 = set2.difference(set1)

        list1 = []
        list2 = []

        for i in diff1: 
            list1.append(i)

        for i in diff2: 
            list2.append(i)    

        res.append(list1)
        res.append(list2)

        return res