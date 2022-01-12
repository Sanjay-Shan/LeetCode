# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.root=None
    
    def traverse(self):
        root=self.root
        while root is not None:
            print(root.val)
            root=root.next
        
    def deleteNode(self,node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.next.val,node.val=node.val,node.next.val
        print(node.val,node.next.val)
        node.next=node.next.next