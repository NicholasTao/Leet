class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.compress(S) == self.compress(T)
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
    s = "abb#c"
    t = "ac#b#bc"
    print(Solution().backspaceCompare(s, t))
