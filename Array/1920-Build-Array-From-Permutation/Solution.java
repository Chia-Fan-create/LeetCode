// package leetcode;
import java.util.Arrays; // Import Arrays for printing arrays

class Solution {
    // Method to build array based on permutation
    public int[] buildArray(int[] nums) {
        // Create a new array 'ans' with the same length as 'nums' to store the result
        int[] ans = new int[nums.length];
        
        // Iterate through each index 'i' of the 'nums' array
        for (int i = 0; i < nums.length; i++) {
            // Set ans[i] to nums[nums[i]] as per the problem's requirement
            ans[i] = nums[nums[i]];
        }
        
        // Return the constructed array 'ans'
        return ans;
    }

    // Main method to test the buildArray function with custom test cases
    public static void main(String[] args) {
        // Create an instance of Solution to call the non-static buildArray method
        Solution solution = new Solution();
        
        // Test Case 1: nums = [0,2,1,5,3,4]
        int[] nums1 = {0, 2, 1, 5, 3, 4};
        System.out.println("Test Case 1 Input: " + Arrays.toString(nums1));
        int[] result1 = solution.buildArray(nums1);
        System.out.println("Test Case 1 Output: " + Arrays.toString(result1));
        
        // Test Case 2: nums = [5,0,1,2,3,4]
        int[] nums2 = {5, 0, 1, 2, 3, 4};
        System.out.println("Test Case 2 Input: " + Arrays.toString(nums2));
        int[] result2 = solution.buildArray(nums2);
        System.out.println("Test Case 2 Output: " + Arrays.toString(result2));
    }
}
