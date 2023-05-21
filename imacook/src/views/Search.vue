<template>
  <div class="entete">
    <h1>IMACOOK</h1>
    <a href="index.html" class="accueil">Accueil</a>
    <div class="search">
      <label for="site-search"></label>
      <input type="search" id="site-search" name="q" />
      <a href="recherche.html">
        <img src="image/🦆 icon _search_.png" alt="rechercher" />
      </a>
    </div>
    <a href="ajout.html">
      <img
        src="image/ajoutrecette.png"
        width="40px"
        alt="ajouter une recette"
      />
    </a>
  </div>
  <div class="titre">
    <h2>Résultats :</h2>
  </div>
  <div class="listrecipes">
    <div class="recipe">
      <a href="recette.html">
        <div class="recipeimg">
          <img src="/image/pateboloss.jpg" alt="pates au ketchup" />
        </div>
        <p id="recipe_name">Pates boloss</p>
        <div class="temps">
          <img src="image/🦆 icon _alarm_.png" alt="temps de préparation" />
          <p id="recipe_time">3min24s</p>
        </div>
        <div class="categorie">
          <img src="image/categorie.png" alt="catégorie" />
          <p id="recipe_cat">C.R.O.U.</p>
        </div>
        <div class="cooker">
          <p id="recipe_cat">JeanMich</p>
        </div>
        <div class="bouton">
          <input type="button" value="voir plus" />
        </div>
      </a>
    </div>

    <div class="recipe">
      <a href="recette.html">
        <div class="recipeimg">
          <img src="/image/pateboloss.jpg" alt="pates au ketchup" />
        </div>
        <p id="recipe_name">Pates boloss</p>
        <div class="temps">
          <img src="image/🦆 icon _alarm_.png" alt="temps de préparation" />
          <p id="recipe_time">3min24s</p>
        </div>
        <div class="categorie">
          <img src="image/categorie.png" alt="catégorie" />
          <p id="recipe_cat">C.R.O.U.</p>
        </div>
        <div class="cooker">
          <p id="recipe_cat">JeanMich</p>
        </div>
        <div class="bouton">
          <input type="button" value="voir plus" />
        </div>
      </a>
    </div>
  </div>
</template>
<script setup></script>
<style scoped></style>
