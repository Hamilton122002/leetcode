class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        num = sorted(nums)
        index = num.index(target)
        return index
