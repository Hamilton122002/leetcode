class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c = []
        for i in nums:
            c.append(len([x for x in nums if x < i]))
        return c
