# https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: list) -> int:
        # trasform all Morse Code
        # count them
        # return size of dict

        morseCode = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....",
                     'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...",
                     't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--.."
                     }

        count = {}

        for word in range(len(words)):
            trans = ""
            for i in range(len(words[word])):
                trans += morseCode.get(words[word][i])
            if trans not in count:
                count[trans] = 1
            else:
                count[trans] += 1

        return len(count)


s = Solution()
print(s.uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"]))
