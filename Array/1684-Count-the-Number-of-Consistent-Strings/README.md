# Problem: [Count the Number of Consistent Strings] ([LeetCode #1684](https://leetcode.com/problems/count-the-number-of-consistent-strings/description/?envType=problem-list-v2&envId=array))

### Problem Summary
- Return the number of consistent strings in the array `words`.
- Input: allowed = `String`, words = `list`.
- Output:
### Examples:

```
Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
```


---

### Thought Process
- Initial intuition and how you approached the problem.
- Key observations or patterns noticed.
- Steps of the solution.

---

### Attempts
- **First attempt:** 
Use HashMap to count the character in `allowed` and `words`
Problems:
setting the condition
1. if HashMap_w.keys() == HashMap_w.keys() :
2. if list(HashMap_w.keys()) == list(HashMap_w.keys()) :
3. if sorted(list(HashMap_w.keys())) in sorted(list(HashMap_w.keys())) :
4. if set(list(HashMap_w.keys())) <= set(list(HashMap_w.keys())) :

- **Second attempt:** Don't need to count the number of characters.
- Use list to store the character.

- **Third attempt (if any):** Use check True or False.
- define a function check to check if the word is consistent

---

### Optimizations (Optional)
- Could this be improved further? 
- Alternative approaches you found from editorial or discussions.

---

### What I learned from this problem:
- set() <= set() #python
