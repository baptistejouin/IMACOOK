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

# define route to get all cookers from the database
@app.route('/cookers', methods=['GET'])
def get_cookers():
    conn = sqlite3.connect('database/imacook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes")
    rows = cursor.fetchall()
    conn.close()

    # convert rows to a list of dictionaries
    cookers_list = []
    for row in rows:
        cooker = {
            'id': row[0],
        }
        cookers_list.append(cooker)

    # return the list of cookers as a JSON response
    return jsonify(cookers_list)

if __name__ == '__main__':
    app.run(debug=True)
