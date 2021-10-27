class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balances = defaultdict(int)
        for transaction in transactions:
            lender, borrower, amount = transaction[0], transaction[1], transaction[2]
            balances[borrower] += amount
            balances[lender] -= amount
        borrower, lender = [], []
        for person in balances:
            if balances[person] > 0:
                borrower.append(balances[person])
            elif balances[person] < 0:
                lender.append(balances[person])
        mintran = float('inf')
        nborrower, nlender = len(borrower), len(lender)
        def dfs(ntran, borrowerid):
            if borrowerid == nborrower:
                nonlocal mintran
                mintran = min(mintran, ntran)
                return
            borrowed = borrower[borrowerid]
            for j in range(nlender):
                lent = lender[j]
                if lent == 0:
                    continue
                balance = borrowed + lent
                if balance == 0:
                    borrower[borrowerid] = 0
                    lender[j] = 0
                    dfs(ntran + 1, borrowerid + 1)
                    borrower[borrowerid] = borrowed
                    lender[j] = lent
                    return
            for j in range(nlender):
                lent = lender[j]
                if lent == 0:
                    continue
                balance = borrowed + lent
                if balance > 0:
                    borrower[borrowerid] = balance
                    lender[j] = 0
                    dfs(ntran + 1, borrowerid)
                elif balance < 0:
                    borrower[borrowerid] = 0
                    lender[j] = balance
                    dfs(ntran + 1, borrowerid + 1)
                borrower[borrowerid] = borrowed
                lender[j] = lent
                
        dfs(0, 0)
        return mintran
