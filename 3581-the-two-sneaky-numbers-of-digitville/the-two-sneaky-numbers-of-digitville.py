class Solution:
# try
  def getSneakyNumbers(self, nums: List[int]) -> List[int]:
    d = {}
    ans = []
    for i in nums:
      if i in d:
        ans.append(i)
      else:
        d[i] = i
    return ans