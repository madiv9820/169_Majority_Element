from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Sort the list to group identical elements together
        nums.sort()
        current_Index, n = 0, len(nums)  # Initialize current index and get the length of nums

        # Iterate through the sorted list
        while current_Index < n:
            next_Index = current_Index + 1  # Start checking for duplicates

            # Move next_Index forward while it points to the same element
            while (next_Index < n and 
                   nums[next_Index] == nums[current_Index]):
                next_Index += 1  # Increment next_Index to count duplicates

            # Count how many times the current number appears
            count = next_Index - current_Index
            
            # Check if the count exceeds half the length of nums
            if count > n // 2:
                return nums[current_Index]  # Return the majority element

            current_Index = next_Index  # Move to the next unique element

        return -1  # If no majority element is found, return -1

# Time Complexity: O(n log n), due to the sorting step
# Space Complexity: O(1), since we are modifying the list in place and using a constant amount of extra space