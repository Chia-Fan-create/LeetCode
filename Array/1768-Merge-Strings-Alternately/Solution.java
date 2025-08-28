//package Array.1768-Merge-Strings-Alternately;
import java.util.Arrays; // Import Arrays for printing arrays

public class Solution {
    public String mergeAlternately(String word1, String word2) {
        int i = 0;
        StringBuilder result = new StringBuilder(); // Use StringBuilder with append
        while(i < word1.length() || i < word2.length()) {
            if (i < word1.length()) {
                result.append(word1.charAt(i));
            }
            if (i < word2.length()) {
                result.append(word2.charAt(i));
            }
            i++;
        }
        return result.toString();
    }

    // Main method to test the mergeAlternately function
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test case 1
        String word1 = "abc";
        String word2 = "pqr";
        String merged = solution.mergeAlternately(word1, word2);
        System.out.println(merged);  // Output: "apbqcr"

        // Test case 2
        String word3 = "ab";
        String word4 = "pqrs";
        String merged2 = solution.mergeAlternately(word3, word4);
        System.out.println(merged2);  // Output: "apbqrs"

        // Test case 3
        String word5 = "abcd";
        String word6 = "pq";
        String merged3 = solution.mergeAlternately(word5, word6);
        System.out.println(merged3);  // Output: "apbqcd"
    }

}
