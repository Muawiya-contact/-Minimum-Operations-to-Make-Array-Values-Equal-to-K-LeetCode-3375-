class Solution:
    def minOperations(self, nums, k):
        # If any number is less than k, we can't increase it => impossible
        if any(num < k for num in nums):
            return -1

        from collections import Counter

        freq = Counter(nums)
        unique_values = sorted(freq.keys(), reverse=True)

        operations = 0
        i = 0

        while i < len(unique_values) and unique_values[i] > k:
            curr_val = unique_values[i]
            # Check if this is a valid h:
            # All elements greater than h must be equal (i.e., just this curr_val)
            operations += 1
            i += 1
        return operations

#By Coding Moves

