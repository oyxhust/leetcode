__author__ = 'jimmy'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

if __name__ == "__main__":
    p = ListNode(1)
    p.next = ListNode(2)
    node = ListNode(3)
    p.next.next =node
    p.next.next.next = ListNode(4)
    #print p.next.next.val
    print "%d -> %d -> %d -> %d" % (p.val, p.next.val, p.next.next.val, p.next.next.next.val)
    delete = Solution()
    delete.deleteNode(node)
    print "%d -> %d -> %d" % (p.val, p.next.val, p.next.next.val)