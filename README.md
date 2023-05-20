# IMACOOK

## Programmation Web - IMACS2
Projet mené dans le cadre du cours de programmation web (école d’ingénieurs IMAC).

### Entity Relationship Diagram
![IMACOOK DATABASE](https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81qW7_pMK_wEYukFdvrCWNVlVyCjtr5YWIt35EnZTNbCO29P0Gi6RumYS1zsv_jiGiSlSmZyf8-7O2hYj8ZM_DprMYeQ=w2796-h1582)

**⚠️ Note : Before starting, you need sqlite3, Python3, Pip, and Flask.**

## Init DB (first install only)
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

## Launch App
```bash
# launch the db with sqlite
sqlite3 database/imacook.db

# launch python/flask
flask --app app --debug run
```