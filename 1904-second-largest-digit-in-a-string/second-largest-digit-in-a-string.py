class Solution:

  def secondHighest(self, s: str) -> int:
    st = set()
    for ele in s:
      if "0" <= ele <= "9":
        st.add(int(ele))
    if len(st) <= 1:
      return -1
    li = list(st)
    li.sort()
    return li[-2]