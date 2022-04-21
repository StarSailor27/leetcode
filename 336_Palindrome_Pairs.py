class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        #length = len(words)
        idxList = []
        for i in range(len(words)):
            for j in range(len(words)):
                if(i!=j):
                    
                    #print(concatWord)
                    #print(i,'/',j,'concatWord/reversedWord =',concatWord,concatWord[::-1])
                    
                    #Wrong trial - time over
                    """
                    concatWord = words[i] + words[j]
                    if(concatWord == concatWord[::-1]):
                    #if(concatWord == ''.join(reversed(concatWord))):
                        idxList.append([i,j])
                    """
                    
                    """ Wrong trial2 - time over
                    concatWord = list(words[i] + words[j])
                    for idx in range(int(len(concatWord)/2) + 1):
                        if(concatWord[idx] != concatWord[len(concatWord)-1-idx]):
                            break
                        elif(idx == (int(len(concatWord)/2))):
                            idxList.append([i,j])
                    """
                    
        return idxList