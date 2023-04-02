from LinkedList import ListNode


class Solution:
    def reverseBetween(self, head, left: int, right: int):
        current = head
        counter = 1

        if left == right:
            return head

        while counter + 1 < left:
            current = current.next
            counter += 1

        left_connection = current
        current = current.next
        counter += 1

        new_head = ListNode(current.val)
        previous = new_head

        while counter < right:
            current = current.next
            new = ListNode(current.val, previous)
            previous = new
            counter += 1

        new_head.next = current.next
        current = current.next

        if left > 1:
            left_connection.next = previous
        else:
            new = ListNode(left_connection.val, current)
            new_head.next = new
            return previous

        return head


head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
head2 = ListNode(1, ListNode(2, ListNode(3, None)))

a = Solution()

print(a.reverseBetween(head1, 1, 3))
