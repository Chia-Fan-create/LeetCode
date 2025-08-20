# Problem: [Ｎumber of Good Pairs] ([LeetCode 1512](https://leetcode.com/problems/number-of-good-pairs/description/?envType=problem-list-v2&envId=array))

## Problem Summary
- A "Good Pair" is defined as a pair of indices `(i, j)` where `nums[i] == nums[j]` and `i < j`.
- The task is to count the total number of good pairs in the given list.
- **Input:** A list of integers `nums`.
- **Output:** An integer representing the number of good pairs.

### Example
Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0

---

## Thought Process
- My first idea was to use two nested loops to compare each pair.  
- However, the second loop takes the most time, leading to an inefficient solution.  
- I noticed that using a frequency count of numbers could help reduce the complexity.

---

## Attempts
- **First attempt:** 
for i in range(len(nums)-1):
    j = i + 1
    for j in range(len(nums)-2):
- Problem: j does not always start from i+1 and does not go to the end of the list.


- **Second attempt (if any):** 
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)-1):
- Problem: j does not reach the last element (len(nums) - 1).

---

## Optimizations (Optional)
- HashMap (dictionary) Method
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
    num_count = {} # store count of each number
    count = 0 # total number of good pairs 
    for num in nums:
        if num in num_count: # number already seen before
            count += num_count[num] # form pairs with existing occurrences
            num_count[num] += 1 # increment count
        else:
            num_count[num] = 1 # first time seeing this number
    return count


---

## What I learned from this problem:
- HashMap Method and empty dictionary 
