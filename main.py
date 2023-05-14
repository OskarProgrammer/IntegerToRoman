class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0 
        x = 0
        while x < len(s):
            try:
                if dictionary[s[x]] < dictionary[s[x+1]]:
                    number += (dictionary[s[x+1]]- dictionary[s[x]])
                    x = x+2
                else:
                    number += dictionary[s[x]]
                    x+=1
            except:
                number += dictionary[s[x]]
                x+=1

        return number