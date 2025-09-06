class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # integrate the conditions
                empty_left_plot = (i == 0) or (flowerbed[i-1] == 0) # head or left is empty
                empty_right_plot = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0) # tail or right is empty
                if empty_left_plot and empty_right_plot:
                        flowerbed[i] = 1
                        count += 1
        return count >= n # If count is greater than or equal to n, return True
# Time complexity: O(m) where m is the length of the flowerbed.
# Space complexity: O(1) as we are using a constant amount of extra space.


# Out of runtime
# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         count = 0
#         for i in range(len(flowerbed)):
#             if flowerbed[i] == 0:
#                 if i == 0:
#                     if flowerbed[i+1] == 0: # head
#                         flowerbed[i] = 1
#                         count += 1
#                         print("i=",i,",flowerbed=", flowerbed,",count=", count)
#                 elif i == len(flowerbed): # tail
#                     if flowerbed[i-1] == 0:
#                         flowerbed[i] = 1
#                         count += 1
#                         print("i=",i,",flowerbed=", flowerbed,",count=", count)
#                 else: # other place in list
#                     if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
#                         flowerbed[i] = 1
#                         count += 1
#                         print("i=",i,",flowerbed=", flowerbed,",count=", count)
#         if count >= n:
#             return True
#         else:
#             return False