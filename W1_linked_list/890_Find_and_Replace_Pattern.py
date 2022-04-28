class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        """ Wrong trial 
        #pattern encoding
        tokens = [token for token in list(pattern)]
        
        codePattern = 0
        for i in range(len(tokens)-1):
            if (tokens[i] != tokens[i+1]):
                codePattern += 0x1 << i   
            else:
                codePattern += 0x0 << i
        
        #words encoding
        ansList = []
        
        for word in words:
            divWord = [token for token in list(word)]
            
            codeWord = 0
            for i in range(len(divWord)-1):
                if (divWord[i] != divWord[i+1]):
                    codeWord += 0x1 << i
                else:
                    codeWord += 0x0 << i
                
            if(codePattern == codeWord):
                ansList.append(word)
            
        return ansList
        """        
        #pattern encoding
        tokens = [token for token in list(pattern)]
        lenTokens = len(tokens)
        #tokensTmp = tokens.copy()
        codePattern = 0
        cycle = 0
        for i in range(lenTokens-1):
            for j in range(len(tokens)-1):
                if (tokens[0] != tokens[j+1]):
                    codePattern += 0x1 << cycle
                else:
                    codePattern += 0x0 << cycle
                cycle += 1
            tokens.pop(0)
        print('{0:b}'.format(codePattern))
        
        #words encoding
        ansList = []
        
        for word in words:
            divWord = [token for token in list(word)]
            
            codeWord = 0
            cycle = 0
            for i in range(lenTokens-1):
                for j in range(len(divWord)-1):
                    if (divWord[0] != divWord[j+1]):
                        codeWord += 0x1 << cycle
                    else:
                        codeWord += 0x0 << cycle
                    cycle += 1
                divWord.pop(0)
                
            print('{0:b}'.format(codeWord))
            if(codePattern == codeWord):
                ansList.append(word)   
                
        return ansList