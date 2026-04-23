class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # build counts for s1
        count = {}
        for ch in s1:
            count[ch] = count.get(ch, 0) + 1

        left = 0
        need = len(s1)  # how many chars still needed to match

        for right in range(len(s2)):
            ch = s2[right]
            if ch in count:
                if count[ch] > 0:
                    need -= 1          # this char helps satisfy the need
                count[ch] -= 1          # always decrement inside window

            # keep window size == len(s1)
            if right - left + 1 > len(s1):
                left_ch = s2[left]
                if left_ch in count:
                    count[left_ch] += 1
                    if count[left_ch] > 0:
                        need += 1        # we just removed a helpful char
                left += 1

            if need == 0:
                return True

        return False



            



        
