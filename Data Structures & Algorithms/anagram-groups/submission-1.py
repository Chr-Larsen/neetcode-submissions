class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        inputList = strs.copy()
        returnList = []
        i = 0
        while len(inputList) > 0:
            returnList.append([])
            returnList[i].append(inputList[0])
            j = 1
            while j < len(inputList):
                countS = {}
                countT = {}
                if len(inputList[0]) != len(inputList[j]):
                    j += 1
                    continue
                for k in range(len(inputList[0])):
                    countS[inputList[0][k]] = 1 + countS.get(inputList[0][k], 0)
                    countT[inputList[j][k]] = 1 + countT.get(inputList[j][k], 0)
                if countS == countT:
                    returnList[i].append(inputList[j])
                    inputList.pop(j)
                else:
                    j += 1
            inputList.pop(0)
            i += 1
        return returnList
