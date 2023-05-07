class FreqStack:

    def __init__(self):
        self.freq = {}
        self.stack = [[]]

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = 0
        else:
            self.freq[val] += 1
        if len(self.stack) <= self.freq[val]:
            self.stack.append([])
        self.stack[self.freq[val]].append(val)

    def pop(self) -> int:
        elem = self.stack[-1].pop()
        self.freq[elem] -= 1
        if not self.stack[-1]:
            self.stack.pop()
        if self.freq[elem] < 0:
            self.freq.pop(elem)
        return elem

# https://leetcode.com/problems/maximum-frequency-stack/submissions/945850410/?languageTags=python3
