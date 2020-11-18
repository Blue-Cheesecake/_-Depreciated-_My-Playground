# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution:
    def findRestaurant(self, list1, list2) -> list:
        result = []
        minimum = 2002
        for i in range(len(list2)):
            r1 = list2[i]
            try:
                j = list1.index(r1)
            except ValueError:
                continue
            sumOf = i + j
            if minimum == sumOf:
                result.append(r1)
            if minimum > sumOf:
                result.clear()
                result.append(r1)
                minimum = sumOf

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"], list2=[
          "Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
    # ['Shogun']
    print(s.findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"], list2=[
          "KFC", "Shogun", "Burger King"]))
    # ['Shogun']
    print(s.findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"], list2=[
          "KFC", "Burger King", "Tapioca Express", "Shogun"]))
    # ['KFC', 'Burger King', 'Tapioca Express', 'Shogun']
    print(s.findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"], list2=[
          "KNN", "KFC", "Burger King", "Tapioca Express", "Shogun"]))
    # ['KFC', 'Burger King', 'Tapioca Express', 'Shogun']
    print(s.findRestaurant(list1=["KFC"], list2=["KFC"]))
    # ["KFC"]
    print(s.findRestaurant(["vacag", "KFC"],
                           ["fvo", "xrljq", "jrl", "KFC"]))
    # ['KFC']
