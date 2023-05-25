<template>
  <main>

    <Navbar class="dark"/>
    <div class="titre">
      <h2>Ajout d'une recette</h2>
    </div>
    <form @submit.prevent="submitForm">
      <div>
        <label for="name">Nom de la recette :</label>
        <input type="text" id="name" v-model="recipeName" />
      </div>
      <div>
        <label for="categories">Catégorie :</label>
        <select id="categories" v-model="selectedCategory">
            <option v-for="category in categoriesData" :value="category.id" :key="category.id">
            {{ category.name }}
          </option>
        </select>
      </div>
      <div>
        <label for="cooker">Nom du cuisinier :</label>
        <input type="text" id="cooker" v-model="cookerName" />
      </div>
      <div>
        <label for="difficulty-select">Difficulté :</label>
        <select id="difficulties" v-model="selectedDifficulty">
          <option v-for="difficulty in difficultiesData" :value="difficulty.id" :key="difficulty.id">
            {{ difficulty.label }}
          </option>
        </select>
      </div>
      <div>
        <label for="photo">Photo de la recette :</label>
        <input type="url" id="photo" v-model="photo"/>
      </div>
      <div>
        <label for="timing">Durée de la recette :</label>
        <input type="time" id="timing" v-model="timing" min="00:00" max="50:00" required />
      </div>

      <div>
        <label for="ingredients">Ajout des ingrédients :</label>
        <div v-for="ingredient in ingredientsData" :key="ingredient.id">
          <input type="checkbox" :id="`ingredient-${ingredient.id}`" :value="ingredient.id" v-model="selectedIngredients"/>
          <p>{{ ingredient.name }}</p>
        </div>
      </div>

      <div v-if="selectedIngredients.length > 0">
        <label for="selectedIngredients">Quantité des ingrédients :</label>
        <ul>
          <li v-for="ingredientId in selectedIngredients" :key="ingredientId">
            <p>{{ getIngredientName(ingredientId) }} - Quantité :</p>
            <input type="text" v-model="ingredientQuantities[ingredientId]" :placeholder="`Quantité pour ${getIngredientName(ingredientId)}`"/>
          </li>
        </ul>
      </div>

      <div>
        <label for="tools">Ajout des ustensiles :</label>
        <div v-for="tool in toolsData" :key="tool.id">
          <input type="checkbox" :id="`tool-${tool.id}`" :value="tool.id" v-model="selectedTools" />
          <p>{{ tool.name }}</p>
        </div>
      </div>

      <div>
        <label for="steps">Étapes :</label>
        <div v-for="(step, index) in steps" :key="index">
          <div>
            <label :for="`stepTitle-${index}`">Titre de l'étape :</label>
            <input type="text" :id="`stepTitle-${index}`" v-model="step.title"/>
          </div>
          <div>
            <label :for="`stepDesc-${index}`">Description de l'étape :</label>
            <input type="text" :id="`stepDesc-${index}`" v-model="step.description"/>
          </div>
        </div>
      </div>

      <div>
        <button @click="addStep">Ajouter une étape</button>
      </div>


      <div>
        <input type="submit" value="Valider" />
      </div>
    </form>
  </main>
</template>

<script setup>
import { ref, reactive, watch } from "vue";
import Navbar from "@/components/Navbar.vue";
import axios from "axios";

const categoriesData = ref([]);
const difficultiesData = ref([]);
const ingredientsData = ref([]);
const toolsData = ref([]);

const recipeName = ref("");
const selectedCategory = ref("");
const cookerName = ref("");
const selectedDifficulty = ref("");
const photo = ref("");
const timing = ref("");

const selectedIngredients = ref([]);
const selectedTools = ref([]);
const ingredientQuantities = reactive({});
const steps = reactive({});

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

  function getIngredients() {
  axios
  .get(`http://127.0.0.1:5000/ingredients`)
    .then((response) => {
      ingredientsData.value = response.data;
      console.log(ingredientsData.value);
    })
    .catch((error) => {
      console.error(error);
    });
  }

  function getIngredientName(ingredientId) {
    const ingredient = ingredientsData.value.find((item) => item.id === ingredientId);
    return ingredient ? ingredient.name : "";
  }

  function getTools() {
    axios
    .get(`http://127.0.0.1:5000/tools`)
      .then((response) => {
        toolsData.value = response.data;
        console.log(toolsData.value);
      })
      .catch((error) => {
        console.error(error);
      });
  }

  function addStep() {
    steps.push({ title: '', description: '' });
  }

// Surveiller les changements dans ingredientQuantities et mettre à jour la liste des ingrédients sélectionnés
watch(ingredientQuantities);

  function submitForm() {
  const formData = new FormData();
  formData.append("recipe_name", recipeName.value);
  formData.append("cooker_name", cookerName.value);
  formData.append("photo", photo.value);
  formData.append("category_id", selectedCategory.value);
  formData.append("difficulty_id", selectedDifficulty.value);
  formData.append("timing", timing.value);
  

  axios
    .post("http://127.0.0.1:5000/recipe", formData)
    .then((response) => {
      console.log(response.data);
    })
    .catch((error) => {
      console.error(error);
    });
}

  getCategories();
  getDifficulties();
  getIngredients();
  getTools();

</script>

<style scoped></style>
