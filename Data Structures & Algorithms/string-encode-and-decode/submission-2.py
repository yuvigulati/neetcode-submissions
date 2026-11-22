class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for i in strs:
            encoded_str += str(len(i)) + "#" + i 
        return encoded_str;


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length_of_the_word = int(s[i:j])
            word_start = j + 1
            word_end = word_start + length_of_the_word 

            decoded_strs.append(s[word_start:word_end])
            i = word_end

        return decoded_strs


               




            
