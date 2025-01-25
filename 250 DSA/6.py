class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()

        for num in nums:
            if num in nums_set:
                retuurn True

                nums_set.add(num)

        return False 