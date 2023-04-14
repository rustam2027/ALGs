# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return_str = str(self.val)
        return_str += ' '
        return_str += str(self.next)
        return return_str


def get_Linked_list(value: list) -> ListNode:
    value = value[::-1]
    head = ListNode(value.pop())
    svd_head = head
    while value:
        head.next = ListNode(value.pop())
        head = head.next

    return svd_head
