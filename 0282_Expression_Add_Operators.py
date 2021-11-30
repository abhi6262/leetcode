class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        nlen = len(num)
        expression = []
        output = []
        def dfs(i, target, prev):
            if i == nlen:
                if not target:
                    output.append(''.join(expression))
                return
            curr, start = 0, i
            while i < nlen:
                curr = curr * 10 + int(num[i])
                i += 1
                if not expression:
                    expression.append(str(curr))
                    dfs(i, target - curr, curr)
                    expression.pop()
                    if num[start] == '0':
                        break
                    continue
                expression.append('+')
                expression.append(str(curr))
                dfs(i, target - curr, curr)
                expression[-2] = '-'
                dfs(i, target + curr, -curr)
                expression[-2] = '*'
                dfs(i, target + prev - (prev * curr), prev * curr)
                expression.pop()
                expression.pop()
                if num[start] == '0':
                    break
        dfs(0, target, 0)
        return output
