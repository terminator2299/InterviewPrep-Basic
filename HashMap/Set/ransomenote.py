from typing import Counter


class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:

		hashmap = Counter(magazine) # TC for Counter is O(n)
		for ch in ransomNote:
			if hashmap[ch] > 0:
				hashmap[ch]-=1
			else:
				return False
		return True

	 

	# Time Complexity: O(R + M)  -> R = len(ransomNote), M = len(magazine)

	# Space Complexity: O(M)     -> we're using a hashmap 

	 