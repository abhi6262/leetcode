class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        root  = {}
        output, p_str = set(), []
        empty = set()
        def ispal(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def dfs(n, node):
            #print("dfs", n, node, p_str)
            if '$' in node and ispal("".join(p_str)) and n != node['$']:
                output.add((node['$'], n))
                if len(node.keys()) == 1:
                    #print("here")
                    return
            for child in node:
                if child == '$':
                    continue
                p_str.append(child)
                #print(node[child])
                dfs(n, node[child])
                p_str.pop()
        
        for i, word in enumerate(words):
            if word == "":
                empty.add(i)
                continue
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['$'] = i
        #print("root", root)
        for i, word in enumerate(words):
            curr = root
            l = len(word)
            j = l - 1
            c_str = []
            while j >= 0:
                if word[j] not in curr:
                    break
                if '$' in curr:
                    c_str.append((curr['$'], j))
                    #print("c_str", i, c_str, word)
                curr = curr[word[j]]
                j -= 1
            if j == -1:
                dfs(i, curr)
            if '$' in curr and i != curr['$'] and ispal(word[:j + 1]):
                output.add((curr['$'], i))
            #print("1.", c_str)
            for j, k in c_str:
                #print("c_str here")
                if j != i and ispal(word[:k + 1]):
                    output.add((j, i))
            if empty and ispal(word):
                for key in empty:
                    if key != i:
                        output.add((key, i))
                        #output.append([i, key])
        return [[x, y] for x, y in output]
            
        
