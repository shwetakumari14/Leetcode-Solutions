class Solution:
    def numUniqueEmails(self, emails):
        result = set()

        for email in emails:
            email = email.split("@")
            localName, domainName = email[0], email[1]
            localName = localName.replace(".", "")
            if "+" in localName:
                idx = localName.index("+")
                localName = localName[:idx]
            result.add(localName + "@" + domainName)

        return len(result)

obj = Solution()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
ans = obj.numUniqueEmails(emails)
print(ans)
        