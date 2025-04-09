# 🚀 Minimum Operations to Make Array Values Equal to K

## 📘 Problem Statement

You are given an integer array `nums` and an integer `k`.

You can perform the following operation:

- Choose an integer `h` (called **valid**) such that all elements in `nums` that are **strictly greater than `h` are equal**.
- For each index `i` where `nums[i] > h`, set `nums[i] = h`.

Your goal is to **make all values in `nums` equal to `k`** using the minimum number of operations.  
Return the **minimum number of operations**, or `-1` if it's impossible.

---

## ✅ What is a Valid `h`?

An integer `h` is **valid** if all values in `nums` that are **strictly greater than `h`** are **equal**.

---

## 🧠 Examples

### Example 1

#### Input: nums = [5, 2, 5, 4, 5], k = 2 
#### Output: 2

#### Explanation:

+ Operation 1: Choose h = 4 → nums becomes [4, 2, 4, 4, 4]

+ Operation 2: Choose h = 2 → nums becomes [2, 2, 2, 2, 2]

### Example 2

#### Input: nums = [2, 1, 2], k = 2 
#### Output: -1

#### Explanation: 
There's an element (1) smaller than k, so it's impossible.

### Example 3
#### Input: nums = [9, 7, 5, 3], k = 1 
#### Output: 4

#### Explanation:

+ h = 7 → [7, 7, 5, 3]

+ h = 5 → [5, 5, 5, 3]

+ h = 3 → [3, 3, 3, 3]

+ h = 1 → [1, 1, 1, 1]



---

## 🧩 Constraints

- `1 <= nums.length <= 100`
- `1 <= nums[i], k <= 100`

---

## 💡 Approach

1. **Check for impossibility**: If any element in `nums` is less than `k`, return `-1` (since we can only decrease values).
2. **Sort unique values in descending order**.
3. **Count valid operations** from top down to `k`.

---

## 🧪 Python Code

```python
class Solution:
    def minOperations(self, nums, k):
        if any(num < k for num in nums):
            return -1

        from collections import Counter

        freq = Counter(nums)
        unique_values = sorted(freq.keys(), reverse=True)

        operations = 0
        i = 0

        while i < len(unique_values) and unique_values[i] > k:
            operations += 1
            i += 1

        return operations
```
