class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        #s = s.replace("()", "")
        
        listStr = list(s) # Space Complexity : O(N)
        minMvCnt = len(s) 
        exitCnd = 0
        
        while(exitCnd == 0): # Time Complexity : O(NM)
            for idx in range(len(listStr)-1):
                #print(listStr[idx:idx+2], minMvCnt)
                if (listStr[idx:idx+2] == ['(', ')']):
                    minMvCnt -= 2
                    del listStr[idx:idx+2]
                    break
                if (idx == (len(listStr)-2)):
                    exitCnd = 1
            if (len(listStr) == 0) or (len(listStr) == 1):
                exitCnd = 1
                    
        return(minMvCnt) # O(NM)/O(N)