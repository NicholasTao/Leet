class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s, t = compress(S), compress(T)
        return s == t
    def compress(self, S: str) -> str:
        s = []
        for x in S:
            if x == '#':
                if s:
                    s.pop()
            else:
                s += x
        return ''.join(s)

if __name__ == '__main__':
    sol = Solution()
    print(sol.compress("#6"))
