# Problem: [Reverse Vowels of a String] ([LeetCode #345](hhttps://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75))


### Attempts
- **First attempt:** 
- 1. Build a dictionary to store the index of char and the vowels of string
- 2. Reverse the string using `String[::-1]`
- 3. Build a function "change_char_at_index", slicing the string and replace the char at index

---

### Optimizations (Optional)
- Use Two Pointers method:
- swap the vowels simultaneously
- Use while to start from left and right until they meet.