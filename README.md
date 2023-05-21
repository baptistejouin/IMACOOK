# IMACOOK

## Programmation Web - IMACS2
Projet mené dans le cadre du cours de programmation web (école d’ingénieurs IMAC).

### Entity Relationship Diagram
![IMACOOK DATABASE](https://cdn.discordapp.com/attachments/1092781041342763118/1109525732893397143/dbdiagram.io_d.png)

### Endpoints
_NOTE: See [the documentation of the request](/docs/resquest.md) for more info._
#### Recipes
| status | result | method | endpoint | params |
| --------- | --------- | --------- | --------- | --------- |
| OK | get all recipes | GET | `/recipes` | |
| OK | get one recipe | GET | `/recipe/<id>` | |
| OK | create one recipe | POST | `/recipes/add` | `name`, `cooker`, `picture`, `category_id`, `difficulty_id`, `cooking_time_s`, `[ingredients{"id", "quantity"}]`, `[tools{"id"}]`, `[steps{"title", "description"}]` |
| | delete one recipe | POST | `/recipe/delete/<id>` | | |
#### Ingredients
| status | result | method | endpoint | params |
| --------- | --------- | --------- | --------- | --------- |
| | get all ingredients | GET | `/ingredients` | |
| | get one ingredient | GET | `/ingredient/<id>` | |
#### Categories
| status | result | method | endpoint | params |
| --------- | --------- | --------- | --------- | --------- |
| | get all categories | GET | `/categories` | |
| | get one category | GET | `/category/<id>` | |
#### Difficulty
| status | result | method | endpoint | params |
| --------- | --------- | --------- | --------- | --------- |
| | get all difficulties | GET | `/difficulties` | |
| | get one difficulty | GET | `/difficulty/<id>` | |
#### Tools
| status | result | method | endpoint | params |
| --------- | ---------| --------- | --------- | --------- |
| | get all tools | GET | `/tools` | |
| | get one tool | GET | `/tool/<id>` | |

#### Steps
| status | result | method | endpoint | params |
| --------- | --------- | --------- | --------- | --------- |
| | update the title and description of one step | POST | `/step`
| | delete one step | POST | `/step/delete/<id>` | |
| | create one step | POST | `/step/add` | `[{id_recipe, title, description, step_number}]` |


**⚠️ Note : Before starting, you need sqlite3, Python3, Pip, and Flask.**

### Init DB (first install only)
```bash
# launch the db with sqlite
sqlite3 database/imacook.db

# create the tables
.read database/init.sql

# add fake useful data for debug
.read database/populate.sql

# testing, we should get 3 recipes
SELECT * FROM recipes;

# exit
.exit
```

### Launch App
```bash
# launch the db with sqlite
sqlite3 database/imacook.db

# launch python/flask
flask --app app --debug run
```