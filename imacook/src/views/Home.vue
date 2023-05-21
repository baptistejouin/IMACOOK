<template>
  <main>

    <Navbar class="dark"/>
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
      <div v-for="recipe in recipesData" class="recipe">
        <a :href="`/recipe/${recipe.id}`">
          <div class="recipeimg">
            <img :src="`${recipe.picture}`" :alt="`${recipe.name}`" />
          </div>
          <p id="recipe_name">{{ recipe.name }}</p>
          <div class="temps">
            <img src="image/🦆 icon _alarm_.png" alt="temps de préparation" />
            <p id="recipe_time">{{ parseInt(recipe.cooking_time_s / 60) }} min</p>
          </div>
          <div class="categorie">
            <img src="image/categorie.png" alt="catégorie" />
            <p id="recipe_cat">{{ recipe.category }}</p>
          </div>
        </a>
      </div>
    </div>
  </main>
</template>

<style scope>
.search {
  display: flex;
  align-items: center;
}

a {
  color: black;
  text-decoration: none;
}

.h1 {
  margin: none;
}

.recipe {
  background-color: white;
  display: flex;
  justify-content: center;
  width: calc((100% / 3) - 4vw);
  border-radius: 10%;
  text-align: center;
  color: #7f4e00;
  /* width: fit-content; */
}

.recipeimg {
  border-radius: 50%;
  overflow: hidden;
  margin: 20px;
  height: 15vw;
  width: 15vw;
}

.recipeimg img {
  height: 100%;
}

.temps,
.categorie {
  display: flex;
  align-items: center;
  justify-content: center;
}

.temps img,
.categorie img {
  margin-right: 10px;
  margin-bottom: 5px;
  width: 30px;
}

#recipe_name {
  font-weight: bold;
}

.titre {
  width: 100%;
  display: flex;
  justify-content: space-between;
  margin: 30px;
}

.listrecipes {
  width: 100%;
  display: flex;
  justify-content: space-around;
  gap: 1.25rem;
}
</style>

<script setup>
import { ref } from "vue";
import Navbar from "@/components/Navbar.vue";
import axios from "axios";

const recipesData = ref([]);

function getData() {
  axios
    .get(`http://127.0.0.1:5000/recipes`)
    .then((response) => {
      recipesData.value = response.data;
    })
    .catch((error) => {
      console.error(error);
    });
}

getData();
</script>
