// package Array.1929-Concatenation-of-Array;

public class Solution {
    public int[] getConcatenation(int[] nums) {
        // Version 1: create from Copilot
        int n = nums.length;
        int[] ans = new int[2 * n];
        for (int i = 0; i < n; i++) {
            ans[i] = nums[i];
            ans[i + n] = nums[i];
        }
        return ans;

        // Version 2: create manually
        // int[] newnums = new int[nums.length*2];
        // for (int i = 0; i < (2*nums.length); i++) {
        //     if (i < nums.length) {
        //         newnums[i] = nums[i];
        //     }
        //     else {
        //         newnums[i] = nums[i-nums.length];
        //     }
        // } 
        // return newnums;

        // Version 3: create using index
        // int n=nums.length;
        // int arr[]=new int[2*n];
        // int index=0;
        // for(int i=0;i<n;i++){
        //     arr[index++]=nums[i];
        // } 
        // for(int i=0;i<n;i++){
        //     arr[index++]=nums[i];
        // }
        // return arr;
    }
}
