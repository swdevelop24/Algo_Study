class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0 : return strs
        output = ''
        for string in strs:
            str_len = str(len(string))
            output += str_len + '*' + string
        return output

    def decode(self, s: str) -> List[str]:
        if len(s) == 0: return []
        output = []
        i = 0
        while i < len(s):
            length = ''
            while s[i] != '*':
                length += s[i]
                i += 1
            i+=1
            str_end = i + int(length)
            output.append(s[i:str_end])
            i = str_end
        return output

