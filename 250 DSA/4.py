class Solution:
    def missingNumber(self, nums) -> int:  # No list type hint
        n = len(nums)
        total_sum = (n * (n + 1)) // 2  # Sum of the first 'n' natural numbers
        array_sum = sum(nums)  # Sum of all elements in the array
        return total_sum - array_sum  # Missing number