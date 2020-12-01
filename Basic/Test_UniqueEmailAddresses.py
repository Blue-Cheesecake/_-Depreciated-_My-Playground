# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: list) -> int:
        # TODO clean local name
        # TODO remove duplicate
        # TODO return len the rest

        def clean_local(local: str):
            result = ""
            for i in range(len(local)):
                if local[i] == '+':
                    break
                elif local[i] != '.':
                    result += local[i]
            return result

        for i in range(len(emails)):
            each = emails[i]
            cleaned = ""
            for j in range(len(each)):
                if each[j] == '@':
                    cleaned += clean_local(each[:j])
                    cleaned += each[j:]
                    break
            emails[i] = cleaned

        return len(set(emails))


if __name__ == "__main__":
    s = Solution()
    print(s.numUniqueEmails(emails=["test.email+alex@leetcode.com",
                                    "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
