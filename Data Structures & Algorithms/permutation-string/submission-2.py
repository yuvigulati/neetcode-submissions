class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count = {}

        for i in s1:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        need = len(s1)
        left = 0
        for right in range(len(s2)): 
            if s2[right] in count:
                if count[s2[right]] > 0:
                    need -= 1
                count[s2[right]] -= 1

            if right - left + 1 > len(s1):
                if s2[left] in count:
                    if count[s2[left]] >= 0:
                        need +=1
                    count[s2[left]] += 1
                left += 1
            
            if need == 0:
                return True
        return False
            
                                 
                
                
                

            



            



        
