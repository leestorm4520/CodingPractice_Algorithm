# You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

# You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

# Return a list of all the recipes that you can create. You may return the answer in any order.

# Note that two recipes may contain each other in their ingredients.

 

# Example 1:

# Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
# Output: ["bread"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# Example 2:

# Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
# Example 3:

# Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich","burger"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
# We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
 

# Constraints:

# n == recipes.length == ingredients.length
# 1 <= n <= 100
# 1 <= ingredients[i].length, supplies.length <= 100
# 1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
# recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
# All the values of recipes and supplies combined are unique.
# Each ingredients[i] does not contain any duplicate values.



#Brute Force - too slow
#    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
#         '''
#         recipes, ingredients, supplies
#         from supplies and ingredients --> recipe
        
#         use example 2:
#         bread : yeast and flour
#         -check if yeast in recipe - nope -> check supplies -> yes ->true
#         -check if flour in recipe - nope -> checkk supplies -> yes -> true
#         add to the result list
        
#         sandwich : bread and meat 
#         -check if bread in recipes - yes - check ingredients -> check supplies -> yes ->true
#         -check if meat in recipes - no - check supplies -> yes -> true
#         add to the result list
        
#         recursive type
#         '''
#         result=[]
#         recipeDict={recipes[i]:ingredients[i] for i in range(len(recipes))}
#         flag=False
        
        
#         for ingredients in recipeDict.values():
#             for ingredient in ingredients:
#                 if ingredient in recipeDict.keys():
#                     ingredients.remove(ingredient)
#                     ingredients.extend(recipeDict[ingredient])
#         for recipe, ingredients in recipeDict.items():
#             for ingredient in ingredients:
#                 if ingredient in supplies:
#                     flag=True   
#                 else:
#                     flag=False
#                     break
#             if flag:
#                 result.append(recipe)
        
#         return result

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
         # Construct directed graph and count the in-degrees
        ingredient_to_recipe, in_degree = defaultdict(set), Counter()
        for rcp, ingredient in zip(recipes, ingredients):
            for ing in ingredient:
                ingredient_to_recipe[ing].add(rcp)
            in_degree[rcp] = len(ingredient)
        # Topological sort.    
        ans = []
        for ing in supplies:
            for rcp in ingredient_to_recipe.pop(ing, set()):
                in_degree[rcp] -= 1
                if in_degree[rcp] == 0:
                    supplies.append(rcp)
                    ans.append(rcp)
        return ans
    