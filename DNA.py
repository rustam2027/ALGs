class Solution:
    def findRepeatedDnaSequences(self, s: str):
        seqs = set()
        return_array = set()
        for i in range(len(s) - 10 + 1):
            elem = s[i:i+10]
            if elem in seqs:
                return_array.add(elem)
            seqs.add(elem)
        return list(return_array)

# https://leetcode.com/problems/repeated-dna-sequences/submissions/945854781/
