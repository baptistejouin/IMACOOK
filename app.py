from flask import Flask, jsonify, request
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
    
    if recipe:
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
        return jsonify(recipe), 200
    else:
        conn.close()
        return jsonify({'error': 'Recipe not found'}), 404


@app.route('/recipe/delete/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    # Récupérer la recette avant de la supprimer
    response = get_recipe(recipe_id)
    recipe = response[0]

    if response[1] != 404:
        conn = sqlite3.connect('database/imacook.db')
        cursor = conn.cursor()
        # Supprimer la recette
        cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
        conn.commit()
        conn.close()
        return recipe, 200
    else:
        return jsonify({'error': 'Recipe not found'}), 404

@app.route('/recipe/add', methods=['POST'])
def add_recipe():
    params = request.get_json()

    recipe_name = params["name"]
    recipe_cooker = params["cooker"]
    recipe_picture = params["picture"]
    recipe_category_id = params["category_id"]
    recipe_difficulty_id = params["difficulty_id"]
    recipe_cooking_time_s = params["cooking_time_s"]
    recipe_ingredients = params["ingredients"]
    recipe_steps = params["steps"]
    recipe_tools = params["tools"]

    conn = sqlite3.connect('database/imacook.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO recipes (name, cooker, picture, category_id, difficulty_id, cooking_time_s) VALUES (?, ?, ?, ?, ?, ?)", (recipe_name, recipe_cooker, recipe_picture, recipe_category_id, recipe_difficulty_id, recipe_cooking_time_s))
    conn.commit()

    recipe_id = cursor.lastrowid

    for ingredient in recipe_ingredients:
        cursor.execute("INSERT INTO recipe_ingredient (id_recipe, id_ingredient, quantity) VALUES (?, ?, ?)", (recipe_id, ingredient["id"], ingredient["quantity"]))
        conn.commit()

    for tool in recipe_tools:
        cursor.execute("INSERT INTO recipe_tool (id_recipe, id_tool) VALUES (?, ?)", (recipe_id, tool["id"]))
        conn.commit()
    
    for step in recipe_steps:
        cursor.execute("INSERT INTO steps (id_recipe, step_number, title, description) VALUES (?, ?, ?, ?)", (recipe_id, step["step_number"], step["title"], step["description"]))
        conn.commit()

    recipe = get_recipe(recipe_id)

    conn.close()

    return recipe


if __name__ == '__main__':
    app.run(debug=True)
