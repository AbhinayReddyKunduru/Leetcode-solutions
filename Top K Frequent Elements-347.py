class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        counter_mc=counter.most_common(k)
        return [x[0] for x in counter_mc]