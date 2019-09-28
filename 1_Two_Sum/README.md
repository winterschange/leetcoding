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
题目很简单，就是在一个列表里找出两个数字，是这两个数字的和等于target。<br>
-好久没有做算法题目，手生了，因此先来个暴力搜索，这应该是最原始的想法了吧。:smile:算法复杂度是$o(n^2)$
```Python
def twoSum(self, nums, target):
    # the o(n^2) algorithm
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return i,j 
```
-然后，我们可以想到，对于大于列表中大于target的数，是可以不用考虑的。因此，我们可以使用二分法，进行一个简单的查找，当然，要先排序。
```Python
# find the position of target or the number just small than target
def binarySearch(self, nums, target, low, up):
    while low <= up:
        mid = int((low + up) / 2)
        if target >  nums[mid]:
            low = mid + 1
        elif target < nums[mid]:
            up = mid - 1
        else:
            return mid
    else:
        return up
```
