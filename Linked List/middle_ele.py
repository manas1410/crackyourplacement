'''
Probelm Url-: https://leetcode.com/problems/middle-of-the-linked-list/
'''

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp is not None:
            count+=1
            temp = temp.next
        count1 = 0
        temp = head
        while (temp is not None and count1!=count//2):
            count1+=1
            temp = temp.next
        return temp
