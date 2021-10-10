# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
import random

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        wllen = len(wordlist)
        intersection = defaultdict(lambda: defaultdict(set))
        def candidates(wlist, idx, guess):
            newlist = []
            for i, word in enumerate(wlist):
                if i == idx:
                    continue
                intersect = 0
                for k in range(6):
                    if wlist[i][k] == wlist[idx][k]:
                        intersect += 1
                if intersect == guess:
                    newlist.append(word)
            return newlist
        guess = -1
        secret = 0
        while guess != 6:
            idx = random.randint(0, len(wordlist) - 1)
            guess = master.guess(wordlist[idx])
            if guess != 6:
                wordlist = candidates(wordlist, idx, guess)
