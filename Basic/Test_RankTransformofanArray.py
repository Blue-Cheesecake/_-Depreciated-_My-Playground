from collections import OrderedDict

# ! Time Limit Exceed


class Solution:

    def arrayRankTransform(self, arr: list) -> list:
        # TODO sort --> remove dulicate --> count each --> replace rank
        temp_sort = list(OrderedDict.fromkeys(sorted(arr)))
        ret = arr + []
        rank = 1
        for each in temp_sort:
            count = arr.count(each)
            time = 0
            cont = 0
            while time < count:
                val = arr[cont:].index(each) + cont
                ret[val] = rank
                time += 1
                cont = val + 1
            rank += 1

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.arrayRankTransform(
        arr=[2, -11, 24, 15, 26, -31, -48, -49, 22, 37, -36]))
    # * [6,5,9,7,10,4,2,1,8,11,3]
    print(s.arrayRankTransform(arr=[40, 10, 20, 30]))
    # * [4,1,2,3]
    print(s.arrayRankTransform(arr=[100, 100, 100]))
    # * [1,1,1]
    print(s.arrayRankTransform(arr=[37, 12, 28, 9, 100, 56, 80, 5, 12]))
    # * [5,3,4,2,8,6,7,1,3]
