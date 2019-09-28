## 167. Two Sum II - Input array is sorted
`Easy` [leetcode: Problem 167 (Click this URL)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
### 相似题目：
<table> [1. Two Sum](https://github.com/winterschange/leetcoding/tree/master/1_Two_Sum)
### Description:
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
##### Note:
+ Your returned answers (both index1 and index2) are not zero-based.
+ You may assume that each input would have exactly one solution and you may not use the same element twice.
#### Example:
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```
### Solution:
题目和Problem 1相似，就是在一个列表里找出两个数字，使这两个数字的和等于target。与题目1不同的是，列表是按照从小到大的顺序排列好的。<br>

+ 受到题目1的启发，我们直接使用二分法，二分查找的复杂度是 ![](http://latex.codecogs.com/gif.latex?\\o(log_{2}n))。

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

def twoSum(self, nums, target):
    up = len(nums)-1
    low = 0 
    while nums[low] + nums[up] != target:
        up = self.binarySearch(nums, target - nums[low], low+1, up)
        if nums[low] + nums[up] == target:
            break
        else:
            low += 1
    return low+1, up+1
```
提交！等等……为什么只超过了9%的用户？让我们来看看他们是怎么做的。
```Python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    i = 0
    j = len(numbers) - 1

    while j > i:
        num = numbers[i] + numbers[j]

        if num == target:
            return [i+1, j+1]
        elif num > target:
            j -= 1
        else:
            i += 1
```
原来他们使用了从两头向中间查找的策略，这样在最坏的情况下，需要查找![](http://latex.codecogs.com/gif.latex?\\o(\frac{n}{2}))。
而我们的策略在最坏情况下，需要查找![](http://latex.codecogs.com/gif.latex?\\o(\frac{nlog_{2}n}{2}))。

