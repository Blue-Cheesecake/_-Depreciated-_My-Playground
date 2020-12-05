# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        i = 0
        length = len(address)
        while i < length:
            if address[i] == '.':
                address = address[:].replace(".", "[.]")
                length += 2
                return address
            i += 1

        return address


if __name__ == "__main__":
    s = Solution()
    print(s.defangIPaddr(address="1.1.1.1"))
    print(s.defangIPaddr(address="255.100.50.0"))
    print(s.defangIPaddr("2225.324.2344.234"))
