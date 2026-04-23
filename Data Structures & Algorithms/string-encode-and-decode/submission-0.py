class Solution:
    def encode(self, strs: List[str]) -> str:
        length_of_words = 0
        new_word = ""
        for word in strs:
            length_of_words  = len(word)
            new_word += str(length_of_words) + '#' + word
        return new_word

    def decode(self, s: str) -> List[str]:
        new_list = []
        i = 0 

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length_of_word = int(s[i : j])
            word = s[j + 1 : j + 1 + length_of_word]
            i = j + 1 + length_of_word
            new_list.append(word)
        return new_list

            
