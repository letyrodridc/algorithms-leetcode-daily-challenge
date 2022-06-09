# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = None
        ptr_merged = None
        
        def addNode(value):
            nonlocal merged
            nonlocal ptr_merged 
            
            if merged == None:
                merged = ListNode(val=value)
                ptr_merged = merged
            else:
                ptr_merged.next = ListNode(val=value)
                ptr_merged = ptr_merged.next
        
        ptr_list1 = list1
        ptr_list2 = list2
        
        
        while (ptr_list1 is not None and ptr_list2 is not None):
            if ptr_list1.val < ptr_list2.val:
                addNode(ptr_list1.val)    
                ptr_list1 = ptr_list1.next
            else:
                addNode(ptr_list2.val)    
                ptr_list2 = ptr_list2.next
            
        
        while (ptr_list1 is not None):
            addNode(ptr_list1.val)    
            ptr_list1 = ptr_list1.next
            
            
        while (ptr_list2 is not None):
            addNode(ptr_list2.val)    
            ptr_list2 = ptr_list2.next
            
            
        return merged
        