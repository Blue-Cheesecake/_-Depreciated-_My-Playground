# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/


class Solution:
    def kidsWithCandies(self, candies: list, extraCandies: int):
        # find the maximum
        # if candies[i] + extra >= maximum
        # add True, else: False
        result = []
        fMax = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= fMax:
                result.append(True)
            else:
                result.append(False)
        return result
