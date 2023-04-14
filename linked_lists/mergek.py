from Beep import Beep
from LinkedList import ListNode
from LinkedList import get_Linked_list


class Solution:
    def mergeKLists(self, lists):
        heap = Beep([], [])
        for head in lists:
            if head:
                heap.insert(head.val, head)  # Put all heads into heap

        svd_new_head = None

        if heap:
            new_head = heap.extract_min()  # Get min head and put it to new_head
            svd_new_head = new_head        # Save new head

        while heap:                    # While heap is not empty
            current = new_head.next    # Save next of new_head

            if current is not None:    # check if current is None
                heap.insert(current.val, current)  # Put current into heap (instead new_head)

            new_head.next = heap.extract_min()     # Get next min new_head and link it
            new_head = new_head.next               # Move

        return svd_new_head


lists: list = [get_Linked_list([-4]),
                get_Linked_list([-10,-6,-6]),
                get_Linked_list([0,3]),
                get_Linked_list([2]),
                get_Linked_list([-10,-9,-8,3,4,4]),
                get_Linked_list([-10,-10,-8,-6,-4,-3,1]),
                get_Linked_list([2]),
                get_Linked_list([-9,-4,-2,4,4]),
                get_Linked_list([-4,0])]

print(lists)

print(Solution.mergeKLists(Solution(), lists))
