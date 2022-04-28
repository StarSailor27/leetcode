class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        maxLen = 3
        targetWord = ''
        targetList = []
        targetResult = []
        finalResult = []

        # products sorted lexicographically
        sortedList = products.copy()
        sortedList.sort()
        
        for words in searchWord:
            targetWord = targetWord + words
            targetList.append(targetWord)

        print('products = ', products)
        print('sortedList = ', sortedList)
        
        print('targetList = ', targetList)
        for target in targetList:
            for cmpWord in sortedList:
                #print('target/cmpWord = ', target, '/', cmpWord[0:len(target)])
                if (target == (cmpWord[0:len(target)])):
                    targetResult.append(cmpWord)
                #print(len(targetResult))
                if (len(targetResult) == maxLen):
                    break
            
            print(targetResult)
            finalResult.append(targetResult.copy())
            targetResult.clear()
            
        return finalResult
            
        