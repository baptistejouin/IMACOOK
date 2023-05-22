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
        <select id="categories" v-model="isSelected">
          <template v-for="category in categoriesData" >
            <option :value="category.id">{{ category.name}}</option>
          </template>
        </select>
      </div>
      <div>
        <label for="cooker">Nom du cuisinier :</label>
        <input type="text" id="cooker" name="cooker_name" />
      </div>
      <div>
        <label for="difficulty-select">Difficulté :</label>
        <select id="difficulties" v-model="isSelected">
          <template v-for="difficulty in difficultiesData" >
            <option :value="difficulty.id">{{ difficulty.label}}</option>
          </template>
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
import { ref } from "vue";
import Navbar from "@/components/Navbar.vue";
import axios from "axios";

const categoriesData = ref([]);
const difficultiesData = ref([]);

function getCategories() {
  axios
  .get(`http://127.0.0.1:5000/categories`)
    .then((response) => {
      categoriesData.value = response.data;
      console.log(categoriesData.value);
    })
    .catch((error) => {
      console.error(error);
    });
  }

  function getDifficulties() {
  axios
  .get(`http://127.0.0.1:5000/difficulties`)
    .then((response) => {
      difficultiesData.value = response.data;
      console.log(difficultiesData.value);
    })
    .catch((error) => {
      console.error(error);
    });
  }

  getCategories();
  getDifficulties();
</script>

<style scoped></style>
