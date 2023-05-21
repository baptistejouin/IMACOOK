from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

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
  
# define route to get a specific recipe from the database
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

# define route to delete a specific recipe
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

# define route to get all ingredients from the database
@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    conn = sqlite3.connect('database/imacook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ingredients")
    ingredients_rows = cursor.fetchall()

    ingredients_list = []
    for ingredient in ingredients_rows:
        ingredient_data = {
            'id': ingredient[0],
            'name': ingredient[1]
        }
        ingredients_list.append(ingredient_data)

    conn.close()

    # return the list of ingredients
    return jsonify(ingredients_list)

# define route to get a specific ingredient from the database
@app.route('/ingredient/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id):
    conn = sqlite3.connect('database/imacook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM ingredients WHERE id = ? LIMIT 1", (ingredient_id,))
    ingredient_row = cursor.fetchone()

    if not ingredient_row:
       return jsonify({'error': 'Ingredient not found'}), 404

    ingredient_data = {
        'id': ingredient_row[0],
        'name': ingredient_row[1]
    }

    conn.close()

    # return the ingredient
    return jsonify(ingredient_data), 200

# define route to get all categorys from the database
@app.route('/categories', methods=['GET'])
def get_categories():
    conn = sqlite3.connect('database/imacook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    categories_rows = cursor.fetchall()

    categories_list = []
    for category in categories_rows:
        category_data = {
            'id': category[0],
            'name': category[1]
        }
        categories_list.append(category_data)

    conn.close()

    # return the list of categories
    return jsonify(categories_list)

# define route to get a specific category from the database
@app.route('/category/<int:category_id>', methods=['GET'])
def get_category(category_id):
    conn = sqlite3.connect('database/imacook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM categories WHERE id = ? LIMIT 1", (category_id,))
    category_row = cursor.fetchone()

    if not category_row:
       return jsonify({'error': 'category not found'}), 404

    category_data = {
        'id': category_row[0],
        'name': category_row[1]
    }

    conn.close()

    # return the category
    return jsonify(category_data), 200

# define route to get all difficulties from the database
@app.route('/difficulties', methods=['GET'])
def get_difficulties():
    conn = sqlite3.connect('database/imacook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM difficulty")
    difficulties_rows = cursor.fetchall()

    difficulties_list = []
    for difficulty in difficulties_rows:
        difficulty_data = {
            'id': difficulty[0],
            'label': difficulty[1]
        }
        difficulties_list.append(difficulty_data)

    conn.close()

    # return the list of difficulties
    return jsonify(difficulties_list)

# define route to get a specific difficulty from the database
@app.route('/difficulty/<int:difficulty_id>', methods=['GET'])
def get_difficulty(difficulty_id):
    conn = sqlite3.connect('database/imacook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, label FROM difficulty WHERE id = ? LIMIT 1", (difficulty_id,))
    difficulty_row = cursor.fetchone()

    if not difficulty_row:
       return jsonify({'error': 'difficulty not found'}), 404

    difficulty_data = {
        'id': difficulty_row[0],
        'label': difficulty_row[1]
    }

    conn.close(), 200

    # return the difficulty
    return jsonify(difficulty_data)

# define route to get all tools from the database
@app.route('/tools', methods=['GET'])
def get_tools():
    conn = sqlite3.connect('database/imacook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tools")
    tools_rows = cursor.fetchall()

    tools_list = []
    for tool in tools_rows:
        tool_data = {
            'id': tool[0],
            'name': tool[1]
        }
        tools_list.append(tool_data)

    conn.close()

    # return the list of tools
    return jsonify(tools_list)

# define route to get a specific tool from the database
@app.route('/tool/<int:tool_id>', methods=['GET'])
def get_tool(tool_id):
    conn = sqlite3.connect('database/imacook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM tools WHERE id = ? LIMIT 1", (tool_id,))
    tool_row = cursor.fetchone()

    if not tool_row:
       return jsonify({'error': 'tool not found'}), 404

    tool_data = {
        'id': tool_row[0],
        'name': tool_row[1]
    }

    conn.close()

    # return the tool
    return jsonify(tool_data), 200

# define route to get a specific step from the database
@app.route('/step/<int:step_id>', methods=['GET'])
def get_step(step_id):
    conn = sqlite3.connect('database/imacook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM steps WHERE id = ? LIMIT 1", (step_id,))
    step_row = cursor.fetchone()

    if not step_row:
       return jsonify({'error': 'step not found'}), 404

    step_data = {
        'id': step_row[0],
        'id_recipe': step_row[1],
        'step_number': step_row[2],
        'title': step_row[3],
        'description': step_row[4]
    }

    conn.close()

    # return the step
    return jsonify(step_data), 200

# define route to delete a specific step
@app.route('/step/delete/<int:step_id>', methods=['DELETE'])
def delete_step(step_id):
    # Récupérer la recette avant de la supprimer
    response = get_step(step_id)
    step = response[0]

    if response[1] != 404:
        conn = sqlite3.connect('database/imacook.db')
        cursor = conn.cursor()
        # Supprimer l'étape
        cursor.execute("DELETE FROM steps WHERE id = ?", (step_id,))
        conn.commit()
        conn.close()
        return step, 200
    else:
        return jsonify({'error': 'step not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
