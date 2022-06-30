class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_table = {} # Space compleixty = O(N)
        th_num = int(len(nums)/2) 
        
        for num in nums: # Time complexity = O(N)
            if num in hash_table:
                hash_table[num] += 1
                if (hash_table[num] > th_num):
                    return num
            else:
                hash_table[num] = 1
        
        return nums[0] # corner case : The number of inputs is 1