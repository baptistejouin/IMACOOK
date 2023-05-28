<template>
  <main>
    <Navbar class="dark" />

    <div class="accueil_nav">
      <div class="accueil_title">
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
        <h2>Les recettes populaires</h2>
      </div>
      <div class="radio">
        <input
          type="radio"
          label="Tout afficher"
          id="all"
          name="filter"
          value="-1"
          v-model="isSelected"
        />

        <template v-for="category in categoriesData" :key="category.id">
          <input
            type="radio"
            :label="category.name"
            :id="`category-${category.id}`"
            :value="category.id"
            v-model="isSelected"
          />
        </template>
      </div>
    </div>
    <div class="listrecipes_accueil" recipecontainer>
      <template v-for="recipe in recipesData">
        <div
          v-show="isSelected == recipe.category.id || isSelected == -1"
          class="recipe_accueil"
        >
          <router-link :to="`/recipe/${recipe.id}`">
            <div
              class="accueil-info accueil-img"
              :style="`background-image: url('${recipe.picture}')`"
            ></div>
            <div class="accueil-info">
              <p id="recipe_name">{{ recipe.name }}</p>
            </div>
            <div class="accueil-info">
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
            <div class="accueil-info">
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
          </router-link>
        </div>
      </template>
    </div>
  </main>
</template>

<script setup>
import { ref } from "vue";
import { API_ENDPOINT } from "@/app.config.js";
import Navbar from "@/components/Navbar.vue";
import axios from "axios";

const recipesData = ref([]);
const categoriesData = ref([]);
const isSelected = ref("-1");

function getData() {
  axios
    .get(`${API_ENDPOINT}/recipes`)
    .then((response) => {
      recipesData.value = response.data;
    })
    .catch((error) => {
      console.error(error);
    });
}

function getCategories() {
  axios
    .get(`${API_ENDPOINT}/categories`)
    .then((response) => {
      categoriesData.value = response.data;
      console.log(categoriesData.value);
    })
    .catch((error) => {
      console.error(error);
    });
}

getData();
getCategories();
</script>
