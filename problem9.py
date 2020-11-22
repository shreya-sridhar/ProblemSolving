    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode: 
        dummy = ListNode()
        head = dummy
        while l1 and l2:
            if l1.val>l2.val:
                dummy.next=l2
                l2=l2.next
            else:
                dummy.next=l1
                l1=l1.next
            dummy=dummy.next
        dummy.next = l1 if l1 else l2
        return head.next