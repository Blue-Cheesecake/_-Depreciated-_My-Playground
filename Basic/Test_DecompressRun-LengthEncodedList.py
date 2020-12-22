# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: list) -> list:
        result = []
        i = 0
        while i < len(nums) - 1:
            freq = nums[i]
            val = nums[i+1]

            generate = []
            j = 0
            while j < freq:
                generate.append(val)
                j += 1

            result.extend(generate)
            i += 2

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.decompressRLElist(nums=[1, 2, 3, 4]))
    print(s.decompressRLElist(nums=[1, 1, 2, 3]))
