# Leetcode Q18 4sum

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        return_list = []
        
        for i in range(n - 3):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                # Skip duplicate values for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Initialize two pointers
                left, right = j + 1, n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        # Found a valid quadruplet
                        return_list.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicate values for the third number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicate values for the fourth number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # Move pointers
                        left += 1
                        right -= 1
        
        return return_list

# Example usage:
sol = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(sol.fourSum(nums, target))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]