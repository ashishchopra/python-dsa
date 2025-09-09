class Solution:
    def majority_element(self, arr):
        item_freq = {}
        arr_len = len(arr)
        for item in arr:
            if item in item_freq:
                item_freq[item] += 1
            else:
                item_freq[item] = 1
            if item_freq[item] > arr_len / 2:
                return item
        return -1


solution = Solution()
arr = [2, 13]
major_element = solution.majority_element(arr)
print(major_element)