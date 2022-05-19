class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        minVal = 1000
        nums.sort()
        for i in range(len(nums)):
            
            l, m, r = 0, i+1, len(nums)-1
            
            while(l<m and m<r): # Time complexity = O(N^2) - for + while
                sumVal = sum((nums[l], nums[m], nums[r])) # Space complexity = O(1)
                #print(f'num[{l}] = {nums[l]}, num[{m}] = {nums[m]}, num[{r}] = {nums[r]}, sum={sumVal}, min={minVal}')
                if(abs(sumVal-target) < abs(minVal)):
                    minVal = sumVal-target
                
                if(sumVal < target):
                    l += 1
                elif(sumVal > target):
                    r -= 1
                else:
                    break
        
        return minVal+target