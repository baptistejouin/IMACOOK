<template>
  <main>

    <Navbar class="dark"/>
      <input v-model="search" placeholder="Recherche..." />

    <div class="listrecipes">
      <template v-for="recipe in filteredRecipes" :key="recipe.id">
        <div class="recipe">

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
              <p id="recipe_cat">{{ recipe.category.name }}</p>
            </div>
          </a>
        </div>
        </template>
    </div>
  </main>
</template>
<script setup>
import { ref, watch } from "vue";
import Navbar from "@/components/Navbar.vue";
import axios from "axios";

const recipesData = ref([]);
const filteredRecipes = ref([]);
const search = ref('');

function getData() {
  axios
    .get(`http://127.0.0.1:5000/recipes`)
    .then((response) => {
      recipesData.value = response.data;
      filterRecipes();
    })
    .catch((error) => {
      console.error(error);
    });
}

function filterRecipes() {
  const searchTerm = normalizeString(search.value);
  filteredRecipes.value = recipesData.value.filter((recipe) => {
    const recipeName = normalizeString(recipe.name);
    return recipeName.includes(searchTerm);
  });
}

function normalizeString(str) {
  return str
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "");
}

getData();
watch(search, filterRecipes);

</script>
<style scoped></style>
