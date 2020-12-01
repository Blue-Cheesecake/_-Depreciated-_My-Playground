# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: list, word2: list) -> bool:
        # TODO construct word1 and word2
        # TODO compare if it equal
        cmpA = ""
        cmpB = ""
        indexA = 0
        indexB = 0
        lengthA = len(word1)
        lengthB = len(word2)
        while indexA < lengthA or indexB < lengthB:
            if indexA < lengthA:
                cmpA += word1[indexA]
                indexA += 1
            if indexB < lengthB:
                cmpB += word2[indexB]
                indexB += 1

        if cmpA == cmpB:
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]))
    # ! True
    print(s.arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]))
    # ! False
    print(s.arrayStringsAreEqual(
        word1=["abc", "d", "defg"], word2=["abcddefg"]))
    # ! True
