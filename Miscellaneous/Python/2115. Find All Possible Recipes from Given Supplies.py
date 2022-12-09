class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        suppliesSet, ans = set(supplies), []
        recipesMap = {recipes[i]: ingredients[i] for i in range(len(recipes))}

        for recipe in recipesMap:
            if self.canMakeRecipe(recipe, suppliesSet, recipesMap, set()):
                ans.append(recipe)
        
        return ans
    
    def canMakeRecipe(self, target, suppliesSet, recipesMap, seen):
        if target in suppliesSet:
            return True
        if target in seen:
            return False
        if target not in recipesMap:
            return False
        
        seen.add(target)

        for ingredient in recipesMap[target]:
            if not self.canMakeRecipe(ingredient, suppliesSet, recipesMap, seen):
                return False
        
        suppliesSet.add(target)
        return True
        

obj = Solution()
recipes, ingredients, supplies = ["bread","sandwich","burger"], [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], ["yeast","flour","meat"]
ans = obj.findAllRecipes(recipes, ingredients, supplies)
print(ans)
        