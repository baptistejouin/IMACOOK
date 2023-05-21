# Request documentation

## Add a recipe (POST)
```bash
curl --request POST \
  --url 'http://127.0.0.1:5000/recipe' \
  --header 'Content-Type: application/json' \
  --data '{
        "name": "Poulet au curry",
        "cooker": "Moi",  
        "picture": "https://img.cuisineaz.com/660x660/2018/04/25/i139820-.jpeg",
        "category_id": 1,
        "difficulty_id": 1,
        "cooking_time_s": 3600,
        "ingredients": [
            {
                "id": 1,
                "quantity": 1
            },
            {
                "id": 2,
                "quantity": 2
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Etape 1",
                "description": "Faire cuire le poulet"
            },
            {
                "step_number": 2,
                "title": "Etape 2",
                "description": "Faire cuire le riz"
            }
        ],
        "tools": [
            {
                "id": 1
            },
            {
                "id": 2
            }
        ]
    }'
```

## Add a step (POST)
```bash
curl --request POST \
  --url 'http://127.0.0.1:5000/step' \
  --header 'Content-Type: application/json' \
  --data '{
		"id_recipe": 5,
        "step_number": 1,
        "step_title": "Etape 1 (pas facile celle-là)",
        "step_description": "Faire suer les oignons"
    }'
```

## Update a step (PATCH)
Only the elements that need to be changed can be written in the data to be sent.
```bash
curl --request PATCH \
  --url 'http://127.0.0.1:5000/step/3' \
  --header 'Content-Type: application/json' \
  --data '{
        "step_number": 2,
        "title": "Etape 2",
        "description": "Description mise à jour"
    }'
```