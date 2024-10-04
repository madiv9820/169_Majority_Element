from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Create a frequency dictionary to count occurrences of each number in nums
        frequency_Dict = Counter(nums)

        # Iterate through each unique number and its frequency
        for num, frequency in frequency_Dict.items():
            # Check if the frequency is greater than half the length of nums
            if frequency > len(nums) // 2:
                return num  # Return the majority element

        return -1  # If no majority element is found, return -1

# Time Complexity: O(n), where n is the number of elements in nums
# Space Complexity: O(n) for the frequency dictionary storing counts of unique elements