// LeetCode Q35 Search Insert Position 

public class SearchInserPosition {

    // In this case, it will only call the another function
    public static int searchInsert(int[] nums, int target) {
        return divide(nums, target, 0, nums.length - 1);
    }

    //Use divide and conquer strategy
    public static int divide(int[] nums, int target, int start, int end) {

        // start index bigger than end index, it means not found the target, return insection index
        if (start > end) {
            return start; 
        }

        int mid = start + (end - start) / 2;
        if (nums[mid] == target) {
            return mid;
        }

        // if target larger than middle one
        else if (nums[mid] < target) {
            return divide(nums, target, mid + 1, end);
        } 
        
        //if target smaller than middle one
        else {
            return divide(nums, target, start, mid - 1);
        }
    }

    public static void main(String[]args){
        //call the searInsert function
    }
}