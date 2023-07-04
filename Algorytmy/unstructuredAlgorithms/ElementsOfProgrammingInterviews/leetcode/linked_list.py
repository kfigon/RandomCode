from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    prev = None
    while current:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    return prev

def reverseListRec(head: Optional[ListNode]) -> Optional[ListNode]:
    def foo(this, prev):
        if not this:
            return prev
        tmp = this.next
        this.next = prev
        prev = this
        this = tmp
        return foo(this, prev)
    return foo(head, None)


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# https://leetcode.com/problems/merge-two-sorted-lists
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2
    elif not list2:
        return list1

    ptr = None
    if list1.val <= list2.val:
        ptr = list1
        list1 = list1.next
    else:
        ptr = list2
        list2=list2.next
    
    start_node = ptr
    while list1 and list2:
        if list1.val <= list2.val:
            ptr.next = list1
            list1 = list1.next
        else:
            ptr.next = list2
            list2 = list2.next
        ptr = ptr.next
    
    if list1:
        ptr.next = list1
    elif list2:
        ptr.next = list2

    return start_node

# https://leetcode.com/problems/merge-nodes-in-between-zeros
def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    ptr = head
    start_node = ptr
    pre_last = None

    while ptr.next:
        skip_ptr = ptr.next
        running_sum = 0
        while skip_ptr.val != 0:
            running_sum += skip_ptr.val
            skip_ptr = skip_ptr.next
        ptr.val = running_sum
        ptr.next = skip_ptr
        pre_last = ptr
        ptr = ptr.next
    
    # remove last 0
    pre_last.next = None

    return start_node