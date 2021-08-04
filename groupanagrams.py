Given a list of strings, group anagrams together.
Example:
Input:
["eat", "tea", "tan", "ate", "nat", "bat"]
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
All inputs will be in lowercase.
The order of your output does not matter.
Answers should be in thread messages.

List = ["eat", "tea", "tan", "ate", "nat", "bat"]
import collections

def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dict = collections.defaultdict(list)
        for side in strs:
            dict[''.join(sorted(side))].append(side)
        return list(dict.values())

output =[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
