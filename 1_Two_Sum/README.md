## 1. Two Sum
`Easy` [leetcode: Problem 1 (Click this URL)](https://leetcode.com/problems/two-sum/)
### Description:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
#### Example:
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```
### Solution:
好久没有做算法题目，手生了，因此先来个暴力搜索，这应该是最原始的想法了吧。
```Python
        # the o(n^2) algorithm
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j 
```
