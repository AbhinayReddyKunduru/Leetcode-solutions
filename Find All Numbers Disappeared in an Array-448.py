class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        olist=[]
        nums_set=set(nums)
        for i in range(1,len(nums)+1):
            if i not in nums_set:
                olist.append(i)
        return olist