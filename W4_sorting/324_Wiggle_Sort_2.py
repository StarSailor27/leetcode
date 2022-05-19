class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i, num in enumerate(sorted(nums)[::-1]):
            #print("i, num =",i, num)
            nums[(1+2*i) % (len(nums)|1)] = num
            print((1+2*i) % (len(nums)|1))