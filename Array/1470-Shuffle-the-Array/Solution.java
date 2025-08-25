//package Array.1470-Shuffle-the-Array;
import java.util.Arrays; // Import Arrays for printing arrays

public class Solution {
    public int[] shuffle(int[] nums, int n) {
        // Create a new array with the same length as 'nums'(2n)
        int[] result = new int[nums.length];
        // Initiate pointers: i for first half (x1, x2, ...), j for second half (y1, y2, ...)
        int i = 0; // Points to x values (indices 0 to n-1)
        int j = n; // Points to y values (indices n to 2n-1)
        int counter = 0; //Tracks position in result array


        while (counter < nums.length) {
            if (counter % 2 ==0) {
                // For even indices (0, 2, 4, ...), take from the first half
                result[counter] = nums[i];
                i++; // Move to next x value
            } else {
                // For odd indices (1, 3, 5, ...), take from the second half
                result[counter] = nums[j];
                j++; // Move to next y value
            }
            counter++; // Move to next position in result array
        }
        return result;
    }


// Main method to test the shuffle function with custom test cases
    public static void main(String[] args) {
        // Create an instance of Solution to call the non-static shuffle method
        Solution solution = new Solution();
        
        // Test Case 1: nums = [2,5,1,3,4,7], n = 3
        int[] nums1 = {2, 5, 1, 3, 4, 7};
        int n1 = 3;
        System.out.println("Test Case 1 Input: " + Arrays.toString(nums1) + ", n = " + n1);
        int[] result1 = solution.shuffle(nums1, n1);
        System.out.println("Test Case 1 Output: " + Arrays.toString(result1));
        
        // Test Case 2: nums = [1,2,3,4,4,3,2,1], n = 4
        int[] nums2 = {1, 2, 3, 4, 4, 3, 2, 1};
        int n2 = 4;
        System.out.println("Test Case 2 Input: " + Arrays.toString(nums2) + ", n = " + n2);
        int[] result2 = solution.shuffle(nums2, n2);
        System.out.println("Test Case 2 Output: " + Arrays.toString(result2));
    }
}