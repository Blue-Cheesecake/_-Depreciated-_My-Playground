# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # TODO count frequency of magazine and ransomNote
        # TODO check if ransomNote can be contructed (use them all)
        freqNote = {}
        i = 0
        lengthNote = len(ransomNote)
        lengthMaga = len(magazine)
        while i < lengthNote:
            if ransomNote[i] not in freqNote:
                freqNote[ransomNote[i]] = 1
            else:
                freqNote[ransomNote[i]] += 1
            i += 1

        for i in range(lengthMaga):
            if magazine[i] in freqNote:
                freqNote[magazine[i]] -= 1
                if freqNote[magazine[i]] == 0:
                    del freqNote[magazine[i]]
            if len(freqNote) == 0:
                return True

        if len(freqNote) == 0:
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct(ransomNote="aa", magazine="ab"))
    # ! false
    print(s.canConstruct(ransomNote="a", magazine="b"))
    # ! false
    print(s.canConstruct(ransomNote="aa", magazine="aab"))
    # ! True
