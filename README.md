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
