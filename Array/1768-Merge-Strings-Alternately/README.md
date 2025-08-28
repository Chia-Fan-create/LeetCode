# Problem: [Merge Strings Alternately] ([LeetCode #1768](https://leetcode.com/problems/merge-strings-alternately/description/))

### Problem Summary
- The given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, apped the additional letters onto the end of the merged string.
- Input: string
- Output: string

### Examples
- Example 1:
```
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
```
- Example 2:
```
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
```
- Example 3:
```
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
```

---

### Attempts
- **First attempt:** 
Try using fast and slow method to append the string.
Road block: the difference between string and list, how to count the char of string and append string or how to transfer the list to string.

---

### Final Solution
- Use while to think about the condition 


---

### What I learned from this problem:
- While(condition) {}
```
while(condition)
{
    //executes while condition is true
}
for(initialization;condition;update)
{
    //executes while condition is true
}

```

