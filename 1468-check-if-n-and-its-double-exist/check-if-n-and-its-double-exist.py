class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        for i in range(len(arr)):
            d[i] = arr[i]

        for x in range(len(d)):
            for j in d:
                if x != j :
                    if d[x] == 2 * d[j]:
                        return True

        return False
            
