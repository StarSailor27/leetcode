class Solution:
    def minimumSum(self, num: int) -> int:
        numList = [int(n) for n in str(num)] # space complexity - O(N) 
        numList.sort() # time complexity - O(NlogN)
        
        return 10*numList[0] + 10*numList[1] + numList[2] + numList[3]