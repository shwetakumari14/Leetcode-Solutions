class Solution:
    def minimumHealth(self, damage, armor):
        totolDamage, maxDamage = 0, 0

        for damages in damage:
            totolDamage += damages
            maxDamage = max(maxDamage, damages)
        
        
        return totolDamage - min(maxDamage, armor) + 1


obj = Solution()
damage, armor = [2,5,3,4], 7
ans = obj.minimumHealth(damage, armor)
print(ans)