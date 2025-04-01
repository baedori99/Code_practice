# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        current_node = head
        visited = {}

        while current_node and current_node.next:
            if current_node in visited:
                return True
            visited[current_node] = True
            current_node = current_node.next
        return False
