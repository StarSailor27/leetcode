class Solution:
    # O(MN)/O(1)
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        numJwls = 0 # space complexity = O(1)
        for jwl in list(jewels): # time complexity = O(N)
            numJwls += list(stones).count(jwl) # time complexity = O(M)
            
            #total time complexity = O(MN)
            
        print(numJwls)
        return numJwls