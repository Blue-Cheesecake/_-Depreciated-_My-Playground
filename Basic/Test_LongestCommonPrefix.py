# https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/887/

# This code is not optimal (naive solution)

class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) == 0:
            return ""
        word = strs[0]
        length = 1
        count = 0
        while length < len(word) + 1:
            goahead = True
            for eWord in range(1, len(strs)):
                eachWord = strs[eWord]
                if word[0:length] != eachWord[0:length]:
                    goahead = False

            if not goahead:
                if count == 0:
                    return ""
                return word[0:count]

            count += 1
            length += 1
        return word


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(strs=["flower", "flow", "flight"]))
    # "fl"
    print(s.longestCommonPrefix(strs=["dog", "racecar", "car"]))
    # ""
    print(s.longestCommonPrefix(
        ["ower", "owerfewfwefewfewf", "owerewfewfwef"]))
    # "ower"
