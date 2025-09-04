# Problem: [GCD of String] ([LeetCode #1071](https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75))

### Attempts
**First attempt:** \
I tried checking if one string is a substring of the other and then attempting to find a repeating pattern manually.\
Why it failed / was inefficient: 

- This approach was error-prone because substring inclusion alone doesn't guarantee a common divisor. \
- The manual slicing logic was complicated and didn't clearly handle cases where there was no GCD. \
- Hard to write clean code for “no common divisor” cases. 

**Second attempt:** \
I improved it by using the Euclidean algorithm with recursion:

Result / improvement:
- legant solution that mirrors the classic integer GCD using string slicing.\
- Correctly handles all cases, including when there is no common divisor.\
- Any dead ends or mistakes worth remembering.

**Alternative solution (iterative check of divisors):**
Iterates over possible lengths of the base string.\
- Checks if both strings can be formed by repeating the candidate base string.\
- Useful to understand the relationship between string length divisors and repeated patterns.

---

### What I learned from this problem:

#### Euclidean algorithm for strings:

Conceptually similar to finding GCD of numbers.

Recursively reduce the longer string by removing the shorter string's length until lengths match or no GCD exists.

#### Recursion:

How recursion can elegantly reduce the problem size step by step.

#### String properties:

Repetition patterns can be identified by checking divisibility of lengths and repeated substring formation.

Concatenation check (str1 + str2 == str2 + str1) is a quick way to determine if a GCD exists.

#### Problem-solving mindset:

Start simple, check edge cases, then improve efficiency and correctness.

Compare multiple approaches to understand trade-offs (recursion vs iteration).