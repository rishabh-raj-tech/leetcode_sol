class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        li = []
        for i in range(len(matrix[0])):
            x = []
            for j in matrix:
                x.append(j[i])
            li.append(x)

        return li
