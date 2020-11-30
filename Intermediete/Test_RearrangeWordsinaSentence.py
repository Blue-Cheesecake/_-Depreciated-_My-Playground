class Solution:
    def arrangeWords(self, text: str) -> str:
        # TODO split in array
        # TODO find the length of each
        # TODO Capitalize the first, lowercase the rest

        clean = text.split(" ")
        order = []

        for i in range(len(clean)):
            order.append(len(clean[i]))

        string = ""
        order.sort()
        for i in range(len(order)):
            length = order[i]
            # TODO find the length in clean
            for j in range(len(clean)):
                if len(clean[j]) == length:
                    if i == 0:
                        clean[j] = clean[j].lower()
                        clean[j] = clean[j].capitalize()
                    else:
                        clean[j] = clean[j].lower()

                    string += clean[j]
                    clean.pop(j)
                    break

            if i != len(order) - 1:
                string += ' '

        return string


if __name__ == "__main__":
    s = Solution()
    print(s.arrangeWords(
        text="Leetcode is cool"
    ))
    # ! "Is cool leetcode"
    print(s.arrangeWords(
        text="Keep calm and code on"
    ))
    # ! "On and keep calm code"
