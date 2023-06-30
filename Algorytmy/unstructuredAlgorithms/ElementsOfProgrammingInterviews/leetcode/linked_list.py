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