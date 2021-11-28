class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        slen = len(s)
        output = set()
        curr = []
        count = {'(': 1, ')': -1}
        leftrem, rightrem = 0, 0
        for c in s:
            if c.isalpha():
                continue
            if c == '(':
                leftrem += 1
            else:
                if leftrem > 0:
                    leftrem -= 1
                else:
                    rightrem += 1
        def dfs(i, count):
            nonlocal leftrem, rightrem
            if i == slen:
                if not leftrem and not rightrem:
                    output.add(''.join(curr))
                return
            if s[i].isalpha():
                curr.append(s[i])
                dfs(i + 1, count)
                curr.pop()
            else:
                if s[i] == '(':
                    curr.append(s[i])
                    dfs(i + 1, count + 1)
                    curr.pop()
                    if leftrem:
                        leftrem -= 1
                        dfs(i + 1, count)
                        leftrem += 1
                else:
                    if count > 0:
                        curr.append(s[i])
                        dfs(i + 1, count - 1)
                        curr.pop()
                    if rightrem:
                        rightrem -= 1
                        dfs(i + 1, count)
                        rightrem += 1
        dfs(0, 0)
        return list(output)
