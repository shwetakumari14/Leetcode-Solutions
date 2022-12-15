from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        email_accounts_map = defaultdict(list)
        visited_accounts = [False]*len(accounts)
        result = []

        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                email_accounts_map[email].append(i)
        
        def dfs(i, emails):
            if visited_accounts[i]:
                return
            
            visited_accounts[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)

                for neighbours in email_accounts_map[email]:
                    dfs(neighbours, emails)
        
        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            result.append([name] + sorted(emails))
        
        return result


obj = Solution()
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
ans = obj.accountsMerge(accounts)
print(ans)
        