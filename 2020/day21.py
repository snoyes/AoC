from aoc import data
from collections import defaultdict, Counter
import re
def p(line):
    ingredients, allergens = line.split(' (contains ')
    ingredients = ingredients.split(' ')
    allergens = allergens.replace(')', '').split(', ')
    return ingredients, allergens

contents = data(parser=p, delimiter='\n')
recipes = defaultdict(Counter)
ingredients = Counter()
allergens = Counter()
for food in contents:
    ingredients.update(food[0])
    for allergen in food[1]:
        allergens.update([allergen])
        recipes[allergen].update(food[0])

print('allergens', allergens)
print('recipes', recipes)
print('ingredients', ingredients)

couldBe = set()
allergenMap = defaultdict(list)
for allergen, allergenCount in allergens.items():
    allergenMap[allergen] = [ingredient[0] for ingredient in recipes[allergen].items() if ingredient[1] == allergenCount]
    couldBe = couldBe.union(set(allergenMap[allergen]))

print('allergen map', allergenMap)
print('possible allergens', couldBe)
nonAllergenics = {ingredient for ingredient in ingredients.items() if ingredient[0] not in couldBe}
print('non-allergenic', nonAllergenics)
print('part 1:', sum(c for k, c in nonAllergenics))

while any(len(possibleAllergens) > 1 for possibleAllergens in allergenMap.values()):
    for allergen, possibleAllergens in allergenMap.items():
        if len(possibleAllergens) == 1:
            for a in allergenMap:
                if a != allergen and possibleAllergens[0] in allergenMap[a]:
                    allergenMap[a].remove(possibleAllergens[0])

print('allergen map', allergenMap)
print('allergen map keys', sorted(allergenMap.keys()))
print('part2:', ','.join([allergenMap[i] [0] for i in sorted(allergenMap.keys())]))
