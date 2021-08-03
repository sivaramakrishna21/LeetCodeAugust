#Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

#The solution set must not contain duplicate subsets. Return the solution in any order.
#Example 1:

#Input: nums = [1,2,2]
#Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
date: Aug 3

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out=[[]]
        for i in range(1,len(nums)+1):
            out+=self.findSubset(nums,i)
        return out
        
    def findSubset(self,nums,n):
        
        if(n==0):
            return [[]]
        
        flag=[]
        for i in range(len(nums)):
            currentElement=nums[i]
            remainingList=nums[i+1::]
            for j in self.findSubset(remainingList,n-1):
                if sorted([currentElement]+j) not in flag:
                    flag.append(sorted([currentElement]+j))
        # print(flag)
        return flag
            
