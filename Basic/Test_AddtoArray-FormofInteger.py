# https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution:
    def addToArrayForm(self, A: list, K: int) -> list:
        # turn K to string
        # compare either max
        # plus in reverse order
        # and return in original order
        k = str(K)
        k = k[::-1]
        A.reverse()
        plusOne = False
        if len(A) >= len(k):
            for i in range(len(A)):
                if i < len(k):
                    A[i] += int(k[i])
                if plusOne:
                    A[i] += 1
                    plusOne = False
                if A[i] >= 10:
                    A[i] %= 10
                    plusOne = True

            if i + 1 >= len(k):
                if plusOne:
                    A.append(1)

            A.reverse()
            return A

        ret = ''
        for i in range(len(k)):
            hold = 0
            if i < len(A):
                hold = int(k[i]) + A[i]
            else:
                hold = int(k[i])
            if plusOne:
                hold += 1
                plusOne = False
            if hold >= 10:
                hold %= 10
                plusOne = True
            ret += str(hold)

        if plusOne:
            ret += '1'

        ret = ret[::-1]
        ret = list(ret)
        for i in range(len(ret)):
            ret[i] = int(ret[i])
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.addToArrayForm(A=[1, 2, 0, 0], K=34))
    # [1,2,3,4]
    print(s.addToArrayForm(A=[2, 7, 4], K=181))
    # [4,5,5]
    print(s.addToArrayForm(A=[2, 1, 5], K=806))
    # [1,0,2,1]
    print(s.addToArrayForm(A=[9, 9, 9, 9, 9, 9, 9, 9, 9, 9], K=1))
    # [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(s.addToArrayForm(A=[1, 2, 0, 0, 6, 4, 2, 1, 6, 4, 3, 1], K=9999999
                           ))
    # [1,2,0,0,7,4,2,1,6,4,3,0]
    print(s.addToArrayForm(A=[1, 2, 0, 0], K=345465467))
    # [3,4,5,4,6,6,6,6,7]
    print(s.addToArrayForm(A=[1, 2], K=9999))
    # [1,0,0,1,1]
