<template>
	<div class="entete">
        <h1>IMACOOK</h1>
        <a href="index.html" class="accueil">Accueil</a>
        <div class="search">
            <label for="site-search"></label>
            <input type="search" id="site-search" name="q">
            <a href="recherche.html">
                <img src="image/🦆 icon _search_.png" alt="rechercher">
            </a>
        </div>
        <a href="ajout.html">
             <img src="image/ajoutrecette.png" width="40px" alt="ajouter une recette">
        </a>
    </div>
    <div class="titre">
        <h2>Les recettes populaires</h2>
        <div>
            <label for="categories">Filtre</label>
            <select id="categories">
                <option value="option1">Option 1</option>
                <option value="option2">Option 2</option>
                <option value="option3">Option 3</option>
            </select>
        </div>
    </div>
    <div class="listrecipes">
        <div class="recipe">
            <a href="recette.html">
                <div class="recipeimg">
                    <img src="/image/pateboloss.jpg" alt="pates au ketchup">
                </div>
                <p id="recipe_name">Pates boloss</p>
                <div class="temps">
                    <img src="image/🦆 icon _alarm_.png" alt="temps de préparation">
                    <p id="recipe_time">3min24s</p>
                </div>
                <div class="categorie">
                    <img src="image/categorie.png" alt="catégorie">
                    <p id="recipe_cat">C.R.O.U.</p>
                </div>
            </a>
        </div>

        <div class="recipe">
            <a href="recette.html">
                <div class="recipeimg">
                    <img src="/image/pateboloss.jpg" alt="pates au ketchup">
                </div>
                <p id="recipe_name">Pates boloss</p>
                <div class="temps">
                    <img src="image/🦆 icon _alarm_.png" alt="temps de préparation">
                    <p id="recipe_time">3min24s</p>
                </div>
                <div class="categorie">
                    <img src="image/categorie.png" alt="catégorie">
                    <p id="recipe_cat">C.R.O.U.</p>
                </div>
            </a>
        </div>
    </div>
</template>

<style scope>
.entete{
    display: flex;
    justify-content: space-between;
    margin-right: 20px;
    margin-left: 20px;
    align-items: center;
}

.search{
    display: flex;
    align-items: center;
}

a{
    color: black;
    text-decoration: none;
}

.entete h1,
.entete a{
    font-size: 25px;
    color: #D18000;
    text-align: center;
    font-weight: normal;
}

.h1{
    margin: none;
}

.recipe{
    background-color: white;
    width: 20vw;
    border-radius: 10%;
    text-align: center;
    color: #7F4E00;
    width: fit-content;
}

.recipeimg{
    border-radius: 50%;
    overflow: hidden;
    margin: 20px;
    height: 15vw;
    width: 15vw;
}

.recipeimg img{
    height: 100%;
}

.temps, .categorie{
    display: flex;
    align-items: center;
    justify-content: center;
}

.temps img, .categorie img{
    margin-right: 10px;
    margin-bottom: 5px;
    width: 30px;
}

#recipe_name{
    font-weight: bold;
}

.titre{
    display: flex;
    justify-content: space-between;
    margin: 30px;
}

.listrecipes{
    display: flex;
    justify-content: space-around;
}
</style>

<script>
export default {
	name: 'Home'
};
</script>