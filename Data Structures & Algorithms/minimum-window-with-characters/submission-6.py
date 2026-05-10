class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count1 = {}
        for c in t:
            count1[c] = count1.get(c, 0) + 1
        
        stringList = []
        minList = list(s)
        subStringIn = False
        res = ""
        l = 0
        r = 0

        while l + len(t) <= len(s):
            while not all(v <= 0 for v in count1.values()) and r < len(s):
                if s[r] in count1:
                    count1[s[r]] -= 1
                stringList.append(s[r])
                r += 1
            
            while all(v <= 0 for v in count1.values()):
                subStringIn = True
                if len(stringList) < len(minList):
                    minList = stringList[:]

                if s[l] in count1:
                    count1[s[l]] += 1
                l += 1
                stringList.pop(0)
            if r >= len(s):
                break

        if subStringIn == True:
            res = ''.join(minList)
        return res