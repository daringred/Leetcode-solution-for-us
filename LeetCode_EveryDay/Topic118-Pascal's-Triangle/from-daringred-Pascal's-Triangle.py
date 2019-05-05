class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            # 本行元素个数为i+1，全部设为1
            now = [1]*(i+1)
            # 从第三行起，本行的第n个元素等于前一行的第n-1个元素+第n个元素
            if i >= 2:
                for n in range(1,i):
                    now[n] = pre[n-1]+pre[n]
            result.append(now)
            pre = now
        return result