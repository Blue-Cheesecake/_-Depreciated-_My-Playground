# https://leetcode.com/problems/word-subsets/

# ! Solution below is not passed deu to Time Limit
# ! But the logic to solve is passed , (need to be optimized)


class Solution:
    def wordSubsets(self, A, B):

        result = []

        freqSection = []
        for each in B:
            freq = {}
            for word in each:
                if word not in freq:
                    freq[word] = 1
                else:
                    freq[word] += 1
            freqSection.append(freq)

        def addOrNot(freq, each):
            for char in each:
                if char in freq:
                    freq[char] -= 1
                    if freq[char] == 0:
                        freq.pop(char)
                else:
                    if len(freq) == 0:
                        return True
            if len(freq) != 0:
                return False
            return True

        for each in A:
            add = True
            for freqB in freqSection:
                freq = freqB.copy()
                contOrNot = addOrNot(freq, each)
                if not contOrNot:
                    add = False
            if add:
                result.append(each)

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.wordSubsets(A=["acaac", "cccbb", "aacbb",
                           "caacc", "bcbbb"], B=["c", "cc", "b"]))
