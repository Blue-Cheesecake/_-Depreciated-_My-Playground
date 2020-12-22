# https://leetcode.com/problems/reformat-date/

class Solution:
    def reformatDate(self, date: str) -> str:
        month = ("Jan", 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
        d = 2
        ret = ''
        for word in reversed(date.split()):
            if d == 0:
                if len(word) == 3:
                    ret += '0'
                    ret += word[:1]
                else:
                    ret += word[:2]
            else:
                if d == 1:
                    if month.index(word) + 1 < 10:
                        ret += '0'
                    ret += str(month.index(word)+1)
                else:
                    ret += str(word)
                ret += '-'
            d -= 1
        return ret


s = Solution()
print(s.reformatDate(date="6th Jun 1933"))
# 1933-06-06
print(s.reformatDate(date="20th Oct 2052"))
# "2052-10-20"
print(s.reformatDate(date="26th May 1960"))
# 1960-05-26
