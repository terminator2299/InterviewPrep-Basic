from collections import defaultdict

class Solution:
		def maxNumberOfBalloons(self, text: str) -> int:
			counter = defaultdict(int)
			balloon = "balloon"
	
			for c in text:
				if c in balloon:
					counter[c] += 1
	
			if any(c not in counter for c in balloon):
				return 0
	
			else:
				return min(counter["b"], counter["a"], counter["l"] // 2, counter["o"] // 2, counter["n"])
	
	 
	
	# Time Complexity: O(n)
	
	# Space Complexity: O(1)
	
	# The space complexity is O(1) because the size of the counter dictionary is constant,
	# regardless of the size of the input string. It only stores counts for the characters
	# in the word "balloon", which has a fixed length.