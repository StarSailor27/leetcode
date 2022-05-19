class Solution:
    def sortSentence(self, s: str) -> str:
        
        words = s.split()
        sortStc = [0 for x in words] # Space complexity = O(N)
        
        for word in words: # Time complexity = O(N)
            wd, idx = word[:-1], word[-1]
            sortStc[int(idx)-1] = wd
        
        return ' '.join(s for s in sortStc) 