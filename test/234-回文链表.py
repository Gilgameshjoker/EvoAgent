# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

head = [1,2,2,1,3]
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 数组转链表辅助函数
def build_linked_list(arr):
    if not arr:
        return None
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

# 链表打印辅助函数，方便看输出结果
def print_link(head: Optional[ListNode]):
    res = []
    p = head
    while p:
        res.append(str(p.val))
        p = p.next
    print("->".join(res))

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]
        """

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        """
        ## 递归的逻辑是，先一直执行方法中的recursively_check()方法，
        # 一直到current_node.next的最后面的节点，一直递归到最后面的节点之后，再执行print()方法输出节点值
        # 相当于是每次递归其实读取了print()方法但是没执行，最终结束递归的时候按逆序一次性全部执行
        def recursively_check(current_node=head):
            if current_node is not None:
                recursively_check(current_node.next)
                print(current_node.val)
            #return True

        recursively_check()
        """



heada = build_linked_list(head)
solution = Solution()
new_head = solution.isPalindrome(heada)
print(new_head)

#print_link(new_head)