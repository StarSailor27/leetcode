class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        chkTable = [0] * 26 # space complexity : O(N)
        
        for word in list(sentence): # time complexity : O(N)
            chkTable[ord(word)-97] += 1 
        
        if 0 in chkTable: # time complexity : O(N)
            return False
        else:
            return True # O(N)/O(N)