import copy


def part1(ingredients, allergens):
    unique_allergens = set.union(*allergens)
    for allergen in unique_allergens:
        food_allergens = set.intersection(*[food for i, food in enumerate(ingredients) if allergen in allergens[i]])
        if len(food_allergens) > 0:
            for food in ingredients:
                food -= food_allergens
    return sum(len(foods) for foods in ingredients)


def part2(ingredients, allergens):
    identified_ingredients = {}
    poss_ingredients = {}
    unique_allergens = set.union(*allergens)
    for a in unique_allergens:
        poss_ingredients[a] = set.intersection(*[f for i, f in enumerate(ingredients) if a in allergens[i]])

    while len(identified_ingredients) < len(unique_allergens):
        for allergen, foods in poss_ingredients.items():
            if len(foods) == 1:
                food = {foods.pop()}
                for a in poss_ingredients:
                    poss_ingredients[a] -= food
                identified_ingredients[allergen] = food.pop()
    return ",".join(food for allergen, food in sorted(identified_ingredients.items()))


if __name__ == "__main__":
    with open('day21.txt', 'r') as file:
        raw = file.read()
    ingredients = [set(line[:line.index(" (")].split()) for line in raw.splitlines()]
    allergens = [set(line[line.index("contains") + 9:-1].split(", ")) for line in raw.splitlines()]
    print(part1(copy.deepcopy(ingredients), allergens))
    print(part2(ingredients, allergens))
