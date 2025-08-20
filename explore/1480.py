class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newList = []
        for i in range(len(nums)):
            if i == 0:
                newList.append(nums[i])
            else:
                newList.append(newList[i-1] + nums[i])
            # print('the new list:', newList[i])
            # print('nums:', nums[i])
        return newList