from typing import Optional


l1 = [1,2,4,6,8,10]
l2 = [1,3,4,5,7,8]

# l1 = []
# l2 = []

# l1 = []
# l2 = [0]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        val = []
        cur_dt = 0  # 当前指针所取值
        cur1 = list1  # 链表1的head节点
        cur2 = list2  # 链表2的head节点
        while cur1 and cur2: ## 两个链表中但凡有一个还没到尾，就继续执行
            if cur1.val <= cur2.val:
                val.append(cur1.val)
                cur1 = cur1.next
            elif cur1.val > cur2.val:
                val.append(cur2.val)
                cur2 = cur2.next

        while cur1:
            val.append(cur1.val)
            cur1 = cur1.next
        while cur2:
            val.append(cur2.val)
            cur2 = cur2.next
        build_linked_list(val)
        return val

list11 = build_linked_list(l1)
list22 = build_linked_list(l2)
solution = Solution()
new_head = solution.mergeTwoLists(list11,list22)
print(new_head)