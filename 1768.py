class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []    # creating an empty list

        for a,b in zip(word1, word2):   #using zip fn and it'll be like (a,p) (b,q)
            merged.append(a+b)     #appending the zip as a+b

        merged.append(word1 [len(word2):])    #extra string characters
        merged.append(word2 [len(word1):])     #extra string characters

        return "".join(merged)    #returns and joins the extra char
