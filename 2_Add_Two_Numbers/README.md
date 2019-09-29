## 2. Add Two Numbers
`Medium` [leetcode: Problem 2 (Click this URL)](https://leetcode.com/problems/add-two-numbers/)

### Description:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#### Example:
```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```
### Solution:
从直觉上看，这是一个考察链表应用的题目。既然如此，那就练习一下链表的基本操作吧～:smile:主要是遍历链表，新建并不断在尾部插入新的数值。

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:       
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = l1.val + l2.val
        flag = temp // 10
        
        p_node = ListNode(temp % 10)
        l_head = p_node
        
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            temp = l1.val + l2.val + flag
            p_node.next = ListNode(temp % 10)
            flag = temp // 10
            p_node = p_node.next
            
        while l1.next:
            if flag == 0:
                p_node.next = l1.next
                break
            else:
                l1 = l1.next
                temp = l1.val + flag
                flag = temp // 10
                p_node.next = ListNode(temp % 10)
                p_node = p_node.next
                
        while l2.next:
            if flag == 0:
                p_node.next = l2.next
                break
            else:
                l2 = l2.next
                temp = l2.val + flag
                flag = temp // 10
                p_node.next = ListNode(temp % 10)
                p_node = p_node.next
                
        if flag:
            p_node.next = ListNode(1)
            p_node = p_node.next
                
        return l_head
```
+ Runtime: 72 ms, faster than 92.44% of Python3 online submissions for Add Two Numbers.
+ Memory Usage: 13.9 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.

运行时间还可以，但是内存占用有点多。其实可以不用新建链表，直接更改l1的数值即可。

需要注意的点有：
+ 按位相加会有进位；
+ 两个数字长度不同，需要做处理。
+ 失败的案例： l1=[5],l2=[5]。在最后判断进位标志flag并进行处理。

此外，还看到有同学把链表转换成整形，运算后在转换成链表，是个不错的思路。
