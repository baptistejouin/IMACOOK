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
        category_rows = cursor.fetchall()


        recipe = {
            'id': recipe_row[0],
            'name': recipe_row[4],
            'category': category_rows[0][0],
            # 'difficulty': recipe_row[2],
            'cooker': recipe_row[3],
            'cooking_time_s': recipe_row[6],
            'picture': recipe_row[5],
        }
        recipes_list.append(recipe)

    conn.close()

    # return the list of cookers as a JSON response
    return jsonify(recipes_list)

if __name__ == '__main__':
    app.run(debug=True)
