class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxNum = nums[0] # Space complexity = O(1)
        accNum = nums[0] 
        sizeNums = len(nums) 
        
        for i in range(1,sizeNums): # Time complexity = O(N)
            accNum = accNum + nums[i]
            if (accNum > nums[i]):
                if (accNum > maxNum):
                    maxNum = accNum
            else:
                accNum = nums[i]
                if (nums[i] > maxNum):
                    maxNum = nums[i]
                    
        return maxNum
    
        # Summary
        # Total Complexity = O(N)O(1)