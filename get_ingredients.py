import json
import csv
from collections import Counter

def analyze_ingredients(json_file: str, output_file: str):
    with open(json_file, 'r', encoding='utf-8') as f:
        desserts_recipes = json.load(f)

    all_ingredients = []

    for recipe in desserts_recipes:
        all_ingredients.extend(recipe['ingredients'])

    ingredient_counts = Counter(all_ingredients)

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ingredients", "Count"])  
        for ingredient, count in ingredient_counts.most_common():
            writer.writerow([ingredient, count])

    print(f"Analyse des ingrédients sauvegardée dans {output_file}")

analyze_ingredients('desserts_recipes.json', 'ingredient_analysis.csv')