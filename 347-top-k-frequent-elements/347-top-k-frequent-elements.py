from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I will try to solve the problem using defaultdict
        freq=defaultdict(int)
        
        for i in nums:
            freq[i]+=1
        print(freq)
        final=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        print(final)
        return [final[i][0] for i in range(k)]