"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表
"""
from typing import Optional

head = [1,2,3,4,5]

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """这种方法是将 1->2->3->NULL转为 NULL<-1<-2<-3"""
        """
        cur,pre = head,None  #指针定义到头结点,pre翻转之后的链表
        while cur:
        # 这里循环的逻辑是，先暂存下一个节点，然后将当前节点单独分离，再暂存当前节点值，方便下一次循环反向设置next，然后将当前值改为暂存的next，进行下一次循环
            tmp = cur.next  # 暂存后继节点
            cur.next = pre  ## 修改next引用指向
            pre = cur  ## pre暂存cur
            cur = tmp
        return pre
        """

        # 递归写法
        def recur(cur,pre):
            if not cur:
                return pre
            res = recur(cur.next,cur)
            cur.next = pre
            return res
        return recur(head,None)

# 测试：把数组构建成链表，不能直接传 [1,2,3,4,5]
head = build_linked_list([1,2,3,4,5])
solution = Solution()
new_head = solution.reverseList(head)
print_link(new_head)