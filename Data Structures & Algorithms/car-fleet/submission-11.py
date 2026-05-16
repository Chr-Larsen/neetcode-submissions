class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        paired = sorted(zip(position, speed), key=lambda x: x[0])
        position, speed = zip(*paired)

        res = 0
        i = len(position) - 1
        j = len(position) - 2

        while j >= 0:
            while j >= 0 and (target - position[j])/speed[j] <= (target - position[i])/speed[i]:
                j -= 1
            res += 1
            if j != 0:
                i = j
                j -= 1
            else:
                return res+1
            
        return res