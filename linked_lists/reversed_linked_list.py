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

        if left > 1:
            left_connection = current
            current = current.next
            counter += 1

        new_tail = current
        previous = new_tail
        next_link = current.next

        while counter < right:
            current = next_link
            next_link = current.next
            current.next = previous
            previous = current
            counter += 1

        new_tail.next = next_link

        if left > 1:
            left_connection.next = current
            return head
        else:
            return current


head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
head2 = ListNode(1, ListNode(2, ListNode(3, None)))

a = Solution()

print(a.reverseBetween(head1, 2, 3))

# https://leetcode.com/problems/reverse-linked-list-ii/submissions/929538482/
