class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary = {}
        array = []
        for number in nums1:
            if number not in dictionary:
                dictionary[number] = 1
            elif number in dictionary:
                dictionary[nuumber] = dictionary[number] +1
        for number in nums2:
            if number in dictionary and dictionary[number] >=1:
                array.append(number)
                dictionary[number] = dictionary[number]
        return array