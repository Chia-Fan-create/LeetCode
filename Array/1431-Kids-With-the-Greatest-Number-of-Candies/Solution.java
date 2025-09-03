//package 1431-Kids-With-the-Greatest-Number-of-Candies;
import java.util.List;
import java.util.ArrayList;

public class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = 0;
        // Find the maximum number of candies
        for (int candy : candies) {
            if (candy > max) {
                max = candy;
            }
        }
        // Create the result list
        List<Boolean> result = new ArrayList<>();
        for (int candy : candies) {
            // Check if the current kid can have the greatest number of candies
            result.add(candy + extraCandies >= max);
        }

        return result;
    }
}

// My version
// class Solution {
//     public static int findMax(int[] arr) {
//     int max = arr[0];
//         for (int i=1; i < arr.length; i++) {
//             if (arr[i] > max) {
//                 max = arr[i];
//             }
//         }
//         return max;
//     }
//     public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
//         ArrayList<Boolean> results = new ArrayList<>();
//         int max = findMax(candies);
//         for (int j=0; j < candies.length; j++) {
//             if ((candies[j] + extraCandies) >= max) {
//                 results.add(true);
//             }
//             else {
//                 results.add(false);
//             }
//         } 
//         return results;
//     }
// }
