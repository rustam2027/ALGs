from LinkedList import ListNode


class Solution:
    def detectCycle(self, head):
        first = head
        fast = head
        slow = head
        if fast is None:
            return None
        while (not (fast.next is None) and not (fast.next.next is None)):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while True:
                    fast = fast.next
                    if first == slow:
                        return slow
                    while slow != fast:
                        if first == fast:
                            return first
                        fast = fast.next
                    first = first.next
        return None
