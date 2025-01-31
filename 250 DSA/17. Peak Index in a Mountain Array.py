class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = 1, len(arr) -2
        res =r 
        while l<=r:
            pivot = (l+r) //2
            if arr [pivot] > arr[pivot +1]:
                res = min(res,pivot)
                r = pivot -1
            else:
                l = pivot +1
        return res
            