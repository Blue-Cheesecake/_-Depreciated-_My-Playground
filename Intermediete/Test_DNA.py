# https://www.programming.in.th/task/rev2_problem.php?pid=1019

class Solution:
    def longestDNA(self, dna1, dna2):
        # strict dna1 is the longest DNA
        if len(dna1) < len(dna2):
            dna1, dna2 = dna2, dna1

        result = ''
        for idx_dna1 in range(len(dna1) - 1):
            tempResult = ''
            idx_dna2 = 0
            while idx_dna2 < len(dna2) - 1:
                len_to_cmp = 2
                compareDna1 = dna1[idx_dna1:idx_dna1 + len_to_cmp]
                compareDna2 = dna2[idx_dna2:idx_dna2 + len_to_cmp]
                while compareDna1 == compareDna2 and len_to_cmp <= len(dna2):
                    tempResult = compareDna1
                    len_to_cmp += 1
                    compareDna1 = dna1[idx_dna1:idx_dna1 + len_to_cmp]
                    compareDna2 = dna2[idx_dna2:idx_dna2 + len_to_cmp]
                    if len(tempResult) > len(result):
                        result = tempResult
                    if len_to_cmp > len(dna2):
                        break
                idx_dna2 += 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.longestDNA(dna1='AAAACTGCTACCGGT', dna2='CTGAATCTACTGCTATTGCAA'))
    print(s.longestDNA(dna1='AAACTGCACACTGTGTGGGGGACTGGg',
                       dna2='ACTGTGTGTGACACTGACAGTGACTGGGACTGAAGGGGGGG'))
    print(s.longestDNA(dna1='AAACTGCACACTGTGTGGGGGACTGGGTGTGGGGGGTAAACCACAACCCC',
                       dna2='ACTGTGTGTGACACTGACAGTGACTGGGACTGAAGGGGGGGACAAAACCCCAACACACCCCC'))
