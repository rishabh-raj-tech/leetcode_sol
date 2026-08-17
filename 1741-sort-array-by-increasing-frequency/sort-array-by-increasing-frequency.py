class Solution:

  def frequencySort(self, nums: List[int]) -> List[int]:
    d1 = {}
    for ele in nums:
      d1[ele] = d1.get(ele, 0) + 1

    d2 = {}
    for key, value in d1.items():
      if value not in d2:
        d2[value] = []
      d2[value].append(key)

    x = []
    for i in range(1, max(d2) + 1):
      if i in d2:
        l1 = d2.get(i)
        l1.sort(reverse=True)  
        for val in l1:
          x.extend([val] * i)  

    return x