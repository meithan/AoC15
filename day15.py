import sys

def generate_recipes(teaspoons, num_ing):
    sols = []
    if teaspoons == 0:
        return [[0]*num_ing]
    elif num_ing == 1:
        return [[teaspoons]]
    for i in range(teaspoons+1):
        remain = teaspoons - i
        subsols = generate_recipes(remain, num_ing-1)
        for subsol in subsols:
            sols.append([i]+subsol)
    return sols

class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)
    def __repr__(self):
        return "%s: capacity %i, durability %i, flavor %i, texture %i, calories %i" % (self.name, self.capacity, self.durability, self.flavor, self.texture, self.calories)

def recipe_score(ings, recipe):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for i in range(len(ings)):
        capacity += ings[i].capacity*recipe[i]
        durability += ings[i].durability*recipe[i]
        flavor += ings[i].flavor*recipe[i]
        texture += ings[i].texture*recipe[i]
    if capacity < 0 or durability < 0 or \
    flavor < 0 or texture < 0:
        return 0
    else:
        return capacity*durability*flavor*texture

def recipe_calories(ings, recipe):
    calories = 0
    for i in range(len(ings)):
        calories += ings[i].calories*recipe[i]
    return calories
        
# =====================

###fname = sys.argv[1]
##fname = "input15.txt"
##
##ings = []
##f = open(fname)
##for line in f:
##    line = line.replace(":"," ")
##    line = line.replace(","," ")
##    line = line.split()
##    ings.append(Ingredient(line[0], line[2], line[4], line[6], line[8], line[10]))
##    print ings[-1]
##f.close()
##num_ings = len(ings)
##
##best_score = None
##best_recipe = None
##best_score2 = None
##best_recipe2 = None
##for recipe in generate_recipes(100,num_ings):
##    score = recipe_score(ings, recipe)
##    calories = recipe_calories(ings, recipe)
##    if best_score == None or score > best_score:
##        best_score = score
##        best_recipe = recipe
##    if calories == 500 and (best_score2 == None or score > best_score2):
##        best_score2 = score
##        best_recipe2 = recipe   
##        
##print "Best recipe: %s with score %i" % (repr(best_recipe), best_score)
##print "Best recipe with 500 cals: %s with score %i" % (repr(best_recipe2), best_score2)
