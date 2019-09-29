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

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line);
            line = next(lines)
            l2 = stringToListNode(line);
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
