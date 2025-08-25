//package Array.1470-Shuffle-the-Array;
import java.util.Arrays; // Import Arrays for printing arrays
public class Solution_v2 {
    public int[] shuffle(int[] nums, int n) {
        int len = nums.length; // to store the pair of numbers in right half of the original array
        for (int i = n; i < len; i++) {
            nums[i] = (nums[i]* 1024) + nums[i-n];
            // Store the modified value back into the original array
        }
        int index = 0; // to track the position in the result array
        for (int i = n; i < len; i++, index +=2 ) {
            nums[index] = nums[i] % 1024; // Get the original value of the right half
            nums[index + 1] = nums[i] / 1024; // Get the original value of the left half
        }
        return nums;
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
