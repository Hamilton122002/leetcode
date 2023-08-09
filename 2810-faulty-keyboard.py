class Solution:
    def finalString(self, s: str) -> str:
        while "i" in s:
            index = s.index("i")
            f = s[:index][::-1] 
            s = s[index+1:]
            s = "".join([f, s])
        return s
