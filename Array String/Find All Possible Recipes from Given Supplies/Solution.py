# Time Complexity: O(V+E)
# Space Complexity: O(V)

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        recipe_map = {}
        for i in range(len(recipes)):
            recipe_map[recipes[i]] = ingredients[i]
            
        result = []
        for recipe in recipe_map:
            if self.dfs(recipe, recipe_map, supplies, set()):
                result.append(recipe)
        return result
    
    def dfs(self, target, recipe_map, supplies, memo):
        if target in supplies:
            return True
        
        if target not in recipe_map:
            return False
        
        # to prevent exceeding maximum recursion depth
        # in target already in memo, it meant we tried to make it before
        # so we can just return it
        if target in memo:
            return
        memo.add(target)
        
        for ingredient in recipe_map[target]:
            if not self.dfs(ingredient, recipe_map, supplies, memo):
                return False
        supplies.add(target)
        return True
