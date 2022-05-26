class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        hashTable = {} #space complexity: O(N)
        
        for num in nums: #time complexity: O(N)
            if (num in hashTable):
                hashTable[num] += 1
            else:
                hashTable[num] = 1
        
        numGood = 0 #space complexity: O(1)
        for key in hashTable: #time complexity: O(N)
            numGood += (hashTable[key] * (hashTable[key] - 1))/2
                
        return int(numGood) #O(N)/O(N)