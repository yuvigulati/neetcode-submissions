class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        missing = len(t)
        left = 0
        start = 0
        min_len = float("inf")

        for right in range(len(s)):
            if need.get(s[right], 0) > 0:
                missing -= 1
            need[s[right]] = need.get(s[right], 0) - 1

            while missing == 0:
                if right - left + 1 < min_len:
                    start = left
                    min_len = right - left + 1

                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1

                left += 1

        return "" if min_len == float("inf") else s[start:start+min_len]




                    


            

                
            
             
                
                



                    
                
            
            
               
            








        
