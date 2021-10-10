class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        alen = len(arr)
        sarr = [(i, num) for i, num in enumerate(arr)]
        sarr.sort(key = lambda x: (x[1], x[0]))
        stack = []
        smaller, larger = [-1] * alen, [-1] * alen
        for tup in sarr:
            i, num = tup[0], tup[1]
            while stack and stack[-1] < i:
                larger[stack.pop()] = i
            stack.append(i)
        stack = []
        sarr.sort(key = lambda x: -x[1])
        for tup in sarr:
            i, num = tup[0], tup[1]
            while stack and stack[-1] < i:
                smaller[stack.pop()] = i
            stack.append(i)
        odd, even = [False] * alen, [False] * alen
        odd[-1], even[-1] = True, True
        for i in range(alen-2, -1, -1):
            if larger[i] > -1 and even[larger[i]]:
                odd[i] = True
            if smaller[i] > -1 and odd[smaller[i]]:
                even[i] = True
        return sum(odd)
