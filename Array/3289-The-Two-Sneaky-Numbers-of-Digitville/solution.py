class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        HashMap = {}
        result = []
        for i in nums:
            if i in HashMap:
                # HashMap[i] += 1
                result.append(i)
            else:
                HashMap[i] = 1
        # result = []
        # for key, value in HashMap.items():
        #     if value > 1:
        #         result.append(key)
        return result

