<template>
  <main>

    <Navbar class="dark"/>
    <div class="titre">
      <h2>Ajout d'une recette</h2>
    </div>
    <form action="/ma-page-de-traitement" method="post">
      <div>
        <label for="name">Nom de la recette :</label>
        <input type="text" id="name" name="recipe_name" />
      </div>
      <div>
        <label for="cat-select">Catégorie :</label>
        <select name="categories" id="cat-select">
          <option value="dog">Dog</option>
          <option value="cat">Cat</option>
          <option value="hamster">Hamster</option>
          <option value="parrot">Parrot</option>
          <option value="spider">Spider</option>
          <option value="goldfish">Goldfish</option>
        </select>
      </div>
      <div>
        <label for="cooker">Nom du cuisinier :</label>
        <input type="text" id="cooker" name="cooker_name" />
      </div>
      <div>
        <label for="dificulty-select">Difficulté :</label>
        <select name="dificulties" id="dificulty-select">
          <option value="Facile">Facile</option>
          <option value="Moyen">Moyen</option>
          <option value="Difficile">Difficile</option>
        </select>
      </div>
      <div>
        <label for="photo">Photo de la recette :</label>
        <input
          type="file"
          id="photo"
          name="photo"
          accept="image/png, image/jpeg"
        />
      </div>
      <div>
        <label for="timing">Durée de la recette :</label>
        <input
          type="time"
          id="timing"
          name="timing"
          min="00:00"
          max="50:00"
          required
        />
      </div>
      <div>
        <input type="submit" value="Valider" />
      </div>
    </form>
  </main>
</template>

<script setup>
import Navbar from "@/components/Navbar.vue";
</script>

<style scoped></style>
