<template>
  <main>
    <Navbar class="dark" />
    <div class="search_section">
      <input
        class="search-input"
        v-model="search"
        placeholder="Rechercher une recette..."
      />

      <div class="listrecipes">
        <template v-for="recipe in filteredRecipes" :key="recipe.id">
          <router-link class="recipe" :to="`/recipe/${recipe.id}`">
            <div
              class="search-info search-img"
              :style="`background-image: url('${recipe.picture}')`"
            ></div>
            <div class="search-info">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 69.6 64.1">
                <g id="Calque_2" data-name="Calque 2">
                  <g id="Calque_1-2" data-name="Calque 1">
                    <path
                      class="cls-1"
                      d="M64.39,58.92a2,2,0,0,1,0,2.83l-1.77,1.76a2,2,0,0,1-2.83,0l-23-23-23,23a2,2,0,0,1-2.82,0L9.2,61.75a2,2,0,0,1,0-2.83L40.59,27.53c-2.77-5.14-.79-13,5.14-19C52.53,1.74,62,.15,66.81,5s3.24,14.28-3.57,21.09c-5.45,5.45-12.61,7.56-17.72,5.69l-.1.12-4,4Z"
                    />
                    <path
                      class="cls-1"
                      d="M-3.82,11.42h36a2,2,0,0,1,2,2v9a2,2,0,0,1-2,2h-27a11,11,0,0,1-11-11v0a2,2,0,0,1,2-2Z"
                      transform="translate(16.83 -4.79) rotate(45)"
                    />
                  </g>
                </g>
              </svg>
              <p id="recipe_name">{{ recipe.name }}</p>
            </div>
            <div class="search-info">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 58.46 58.46">
                <g id="Calque_2" data-name="Calque 2">
                  <g id="Calque_1-2" data-name="Calque 1">
                    <path
                      class="cls-1"
                      d="M58.27,22a3.63,3.63,0,0,0-2.91-2.45L39.61,17.17,32.54,2.1a3.66,3.66,0,0,0-6.62,0L18.85,17.17,3.1,19.58A3.65,3.65,0,0,0,1,25.74l11.5,11.79L9.82,54.22A3.66,3.66,0,0,0,15.2,58l14-7.77,14,7.77a3.7,3.7,0,0,0,1.77.45,3.62,3.62,0,0,0,2.11-.67,3.66,3.66,0,0,0,1.5-3.57L45.93,37.53l11.5-11.79A3.65,3.65,0,0,0,58.27,22Z"
                    />
                  </g>
                </g>
              </svg>
              <p id="recipe_cat">{{ recipe.category.name }}</p>
            </div>
            <div class="search-info">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 65.05 65.04">
                <g id="Calque_2" data-name="Calque 2">
                  <g id="Calque_1-2" data-name="Calque 1">
                    <path
                      class="cls-1"
                      d="M32.53,0A32.52,32.52,0,1,0,65.05,32.52,32.53,32.53,0,0,0,32.53,0ZM46.2,41.93a2,2,0,0,1-2.76.61L31.22,34.78a2,2,0,0,1-.93-1.69V16.58a2,2,0,0,1,4,0V32l11.29,7.17A2,2,0,0,1,46.2,41.93Z"
                    />
                  </g>
                </g>
              </svg>
              <p id="recipe_time">{{ parseInt(recipe.cooking_time_s / 60) }}</p>
            </div>
          </router-link>
        </template>
      </div>
    </div>
  </main>
</template>
<script setup>
import { ref, watch } from "vue";
import { API_ENDPOINT } from "@/app.config.js";
import Navbar from "@/components/Navbar.vue";
import axios from "axios";

const recipesData = ref([]);
const filteredRecipes = ref([]);
const search = ref("");

function getData() {
  axios
    .get(`${API_ENDPOINT}/recipes`)
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
<style>
.search_section {
  margin-top: 25px;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  flex-wrap: wrap;
  background: var(--third-color);
  padding: var(--padding);
  border-radius: 40px;
}
.search-input {
  background: var(--second-color);
  outline: none;
  border: none;
  width: 100%;
  color: var(--first-color);
  border-radius: 15px;
  padding: 20px;
  font-family: var(--regular-font);
  font-size: var(--normal-font-size);
  font-weight: 600;
}
.search-input::placeholder {
  color: var(--first-color);
}
.listrecipes {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  flex-wrap: wrap;
  width: 100%;
  margin-top: 50px;
}
.recipe {
  width: 100%;
  height: 150px;
  display: flex;
  justify-content: space-between;
  padding: 20px;
  border-radius: 25px;
  background: var(--third-color);
  font-family: var(--regular-font);
  font-size: var(--normal-font-size);
  color: var(--first-color);
  fill: var(--first-color);
  cursor: pointer;
  box-shadow: rgba(149, 157, 165, 0.25) 0px 5px 36px;
  transition: 0.4s;
  margin-bottom: 30px;
}
.recipe:hover {
  box-shadow: rgba(149, 157, 165, 0.15) 0px 5px 18px;
  transform: scale(0.99);
  transition: 0.4s;
}
.search-info {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  width: 20%;
}
.search-info svg {
  width: var(--icon_min_height);
  height: var(--icon_min_height);
  margin-right: 12px;
}
.search-img {
  border-radius: 40px;
  background-size: cover;
  background-repeat: no-repeat;
}
</style>
