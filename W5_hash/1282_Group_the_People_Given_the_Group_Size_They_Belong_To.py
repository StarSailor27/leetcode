class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        hashTable = defaultdict(list) # Space Complexity: O(N)
        grpList = [] # Space Complexity: O(N)
        
        # Make hashTable
        for idx, uID in enumerate(groupSizes): # Time Complexity: O(N)
            hashTable[uID].append(idx)
        
        # Make group List
        for gSize in hashTable: # Time Complexity: O(N)
            print('gSize={0}, len(hashTable[gSize])={1}'.format(gSize, len(hashTable[gSize])))
            if (gSize != len(hashTable[gSize])):
                for grp in self.listSplit(hashTable[gSize], gSize): # Time Complexity: O(N)
                    grpList.append(grp)
            else:
                grpList.append(hashTable[gSize])
        
        return grpList # O(N^2)/O(N)
        
    def listSplit(self, lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]