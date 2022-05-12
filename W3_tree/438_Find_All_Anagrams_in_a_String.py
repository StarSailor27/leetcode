import copy
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        hashTable = list([0 for i in range(26)])
        
        wdwSize = len(p)
        anaIndex = []
        
        for letter in list(p):
            hashTable[self.calKey(letter)] += 1  
            
        for n in range(len(s)-wdwSize+1):
            cmpWord = s[n:n+wdwSize]
            hashTableCopy = copy.deepcopy(hashTable)
            falseCheck = 0
            
            for letter in list(cmpWord):
                hashTableCopy[self.calKey(letter)] -= 1 
                
            for letter in list(p):
                if (hashTableCopy[self.calKey(letter)] != 0):
                    falseCheck = 1
                    break
            
            if(falseCheck == 0):
                anaIndex.append(n)        
        
        return anaIndex
        """ Time over
        hashTable2 = list([0 for i in range(26)])
        for letter in list(p):
            hashTable[self.calKey(letter)] += 1   
            
        for n in range(len(s)-wdwSize+1):
            cmpWord = s[n:n+wdwSize]

            for letter in list(cmpWord):
                hashTable2[self.calKey(letter)] += 1 
            if (hashTable == hashTable2):
                anaIndex.append(n)
            hashTable2 = list([0 for i in range(26)])
        
        return anaIndex
        """
    def calKey(self, letter):
        return int((ord(letter)-97)%26)