from typing import Optional
from typing import ListNode

class Solution:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		curr = head
		prev = None
		while curr:
			temp = curr.next
			curr.next = prev
			prev = curr
			curr = temp
		return prev