class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums.sort()
        nums.append('')
        dic = {}
        cnt = 1
        output = []
        
        #numPrev = nums[0]+1
        print(nums)
        for i in range(len(nums)-1):
            if (nums[i] == nums[i+1]):
                cnt += 1
            else:
                dic[nums[i]] = cnt
                cnt = 1
        
        print(dic)
        dic = dic.items()
        dic = sorted(dic, key=lambda x: x[1], reverse=True)
        #print(dic)
        for num in range(k):
            output.append(dic[num][0])
        
        return output