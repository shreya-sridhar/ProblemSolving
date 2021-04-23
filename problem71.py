class ListNode:
    	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	
	def __str__(self):
		temp = self
		result = []
		while temp != None:
			result.append(str(temp.val))
			temp = temp.next
		result.append(str(None))
		return "->".join(result)

def reorderList(l):
    sl1,sl2 = createTwoLists(l)
    print("list1",sl1,"list1",sl2)
    revList = reverseList(sl2)
    print("reversed list is",revList)
    final_list = combineLists(sl1,revList)
    print("combinedList",final_list)
    return final_list 

def createTwoLists(l):
    list_length = 0
    l_head = l
    while l_head:
        list_length += 1 
        l_head = l_head.next 
    sl1 = l 
    sl2 = l
    length1 = 1
    while length1 < list_length/2:
        length1 += 1
        sl1 = sl1.next 
    sl2 = sl1.next
    sl1.next = None  
    return l, sl2

def reverseList(l):
    head = l
    prev_list = l
    next_list = prev_list.next
    prev_list.next = None 
    while next_list.next:
        temp = next_list.next 
        next_list.next = prev_list
        prev_list = next_list
        next_list = temp
    return next_list

def combineLists(l1,l2):
    head = l1
    curr_list = l1
    while curr_list:
        l2 = curr_list.next 
        curr_list.next = l2
        curr_list = curr_list.next
    if l2:
        curr_list.next = l2 
    return head

l1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
print(l1)
print(reorderList(l1))

