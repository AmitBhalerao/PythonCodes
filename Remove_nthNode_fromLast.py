"""
Python code to remove n th node from last of linkedlist
input:
head of sinlgy linkedlist
node index n to remove

output:
return head of remaining linkedlist
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        end_ptr = head
        n_ptr = head
        
        # advance the leading pointer n times
        for x in range(n):
            # if we get to the end before n, we've got nothing to trim off
            if end_ptr is None:
                return head
            end_ptr = end_ptr.next
        
        # if we got to the end exactly on the nth iteration, we want to trim off the first node
        if end_ptr is None:
            return head.next
        else:
            end_ptr = end_ptr.next
        
        # advance both pointers together until the end_ptr is off the end of the list
        while end_ptr is not None:
            end_ptr = end_ptr.next
            n_ptr = n_ptr.next
        
        n_ptr.next = n_ptr.next.next
        
        return head
