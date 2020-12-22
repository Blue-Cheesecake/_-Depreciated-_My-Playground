# https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/

class Solution:

    def reverseVowels(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1:
            return s

        # ! find index of left_vowels and right_vowels
        def find_index(start_at, s, v, left_or_right):
            if left_or_right:
                for i in range(start_at, len(s)):
                    if s[i] in v:
                        return i
            else:
                i = start_at
                while s[i] not in v and i >= 0:
                    if s[i] in v:
                        return i
                    i -= 1
                return i

        # ! swap two character
        def swap(s, val_left, val_right, left, right):
            links = s[:left]
            mitte = s[left + 1:right]
            richtig = s[right + 1:]
            combine = links + val_right + mitte + val_left + richtig
            return combine

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left = find_index(start_at=0, s=s, v=vowels, left_or_right=True)
        right = find_index(len(s) - 1, s, vowels, False)

        if left is not None and right is not None:
            while left < right:
                temp_left = left + 0
                temp_right = right + 0
                das_resultat = swap(s, s[left], s[right], left, right)
                left = find_index(start_at=left + 1, s=s,
                                  v=vowels, left_or_right=True)
                right = find_index(right - 1, s, vowels, False)
                s = das_resultat

                # ! incase of out of vowels
                if temp_left == left and temp_right == right:
                    break

        return s


if __name__ == "__main__":
    s = Solution()
    print(s.reverseVowels(",."))

    print(s.reverseVowels(s="aA"))
    # ? "Aa"
    print(s.reverseVowels(s="hello"))
    # ? "holle"
    print(s.reverseVowels(s="leetcode"))
    # ? "leotcede"
