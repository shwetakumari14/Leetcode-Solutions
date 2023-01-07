class Solution:
    def checkLeapYear(self, year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def numberOfDays(self, year, month):
        if self.checkLeapYear(year) and month == 2:
            return 29
        elif not self.checkLeapYear(year) and month == 2:
            return 28
        elif month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif month in (4, 6, 9, 11):
            return 30



obj = Solution()
year, month = 2000, 2
ans = obj.numberOfDays(year, month)
print(ans)