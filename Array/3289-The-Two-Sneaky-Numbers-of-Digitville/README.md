# Problem: [The Two Sneaky Numbers of Digitville] ([LeetCode 3289](https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/?envType=problem-list-v2&envId=array))
### What I learned from this problem:
- 1. The use of a HashMap (dictionary) allows for efficient counting of occurrences. \
   This can be useful for problems involving frequency analysis or finding duplicates.
- 2. The method of catch the key/value of dictionary:
```
for key, value in dic.items():
    if value == n:
        result.append(key)

```
- 2. The approach can be optimized by directly appending duplicates to the result list without needing a separate counting step.