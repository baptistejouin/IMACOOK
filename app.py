from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# define MySQL connection parameters
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'imacook'
}

# define route to get all recipes from the database
@app.route('/recipes', methods=['GET'])
def get_recipes():
    conn = sqlite3.connect('database/imacook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes")
    recipes_rows = cursor.fetchall()

    # convert recipes_rows to a list of dictionaries
    recipes_list = []
    for recipe_row in recipes_rows:

        cursor.execute("SELECT name FROM categories WHERE id = ? LIMIT 1", (recipe_row[1],))
        category_row = cursor.fetchone()
        category = category_row[0] if category_row else None


        recipe = {
            'id': recipe_row[0],
            'name': recipe_row[4],
            'category': category,
            # 'difficulty': recipe_row[2],
            'cooker': recipe_row[3],
            'cooking_time_s': recipe_row[6],
            'picture': recipe_row[5],
        }
        recipes_list.append(recipe)

    conn.close()

    # return the list of cookers as a JSON response
    return jsonify(recipes_list)

    # define route to get all recipes from the database
@app.route('/recipe/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    conn = sqlite3.connect('database/imacook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes WHERE id = ? LIMIT 1", (recipe_id,))
    recipe = cursor.fetchone()

    # get categogy name
    cursor.execute("SELECT name FROM categories WHERE id = ? LIMIT 1", (recipe[1],))
    category_row = cursor.fetchone()
    category = category_row[0] if category_row else None

    # get difficulty label
    cursor.execute("SELECT label FROM difficulty WHERE id = ? LIMIT 1", (recipe[2],))
    difficulty_row = cursor.fetchone()
    difficulty = difficulty_row[0] if difficulty_row else None

    # get needed tools
    cursor.execute("SELECT tools.id, tools.name FROM recipe_tool JOIN tools ON tools.id=recipe_tool.id_tool WHERE id_recipe = ?", (recipe_id,))
    tools = cursor.fetchall()
    # tools conversion from table to object
    tool_list = []
    for tool in tools:
        tool_data = {
            'id': tool[0],
            'name': tool[1]
        }
        tool_list.append(tool_data)

    # get needed ingredients
    cursor.execute("SELECT ingredients.id, ingredients.name FROM recipe_ingredient JOIN ingredients ON ingredients.id=recipe_ingredient.id_ingredient WHERE id_recipe = ?", (recipe_id,))
    ingredients = cursor.fetchall()
    # tools conversion from table to object
    ingredient_list = []
    for ingredient in ingredients:
        ingredient_data = {
            'id': ingredient[0],
            'name': ingredient[1]
        }
        ingredient_list.append(ingredient_data)

    recipe = {
            'id': recipe[0],
            'name': recipe[4],
            'category': category,
            'difficulty': difficulty,
            'cooker': recipe[3],
            'cooking_time_s': recipe[6],
            'picture': recipe[5],
            'tools': tool_list,
            'ingredients': ingredient_list
        }

    conn.close()

    # return the list of cookers as a JSON response
    return jsonify(recipe)

@app.route('/recipe/delete/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    conn = sqlite3.connect('database/imacook.db')
    cursor = conn.cursor()

    # Récupérer la recette avant de la supprimer
    cursor.execute("SELECT * FROM recipes WHERE id = ? LIMIT 1", (recipe_id,))
    recipe = cursor.fetchone()

    if recipe:
        # Supprimer la recette de la table "recipes"
        cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
        conn.commit()
        conn.close()
        return jsonify(recipe), 200
    else:
        conn.close()
        return "Recipe not found", 404

if __name__ == '__main__':
    app.run(debug=True)
