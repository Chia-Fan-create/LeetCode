class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        newnums = []
        for i in range(len(nums)):
            newnums.append(nums[nums[i]])
        return newnums