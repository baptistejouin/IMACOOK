<template>
  <main>

    <Navbar class="dark"/>
    <div class="titre">
      <h2>Ajout d'une recette</h2>
    </div>
    <form @submit.prevent="submitForm">
      <div>
        <label for="name">Nom de la recette :</label>
        <input type="text" id="name" v-model="form.recipe_name" />
      </div>
      <div>
        <label for="categories">Catégorie :</label>
        <select id="categories" v-model="form.category_id">
            <option v-for="category in categoriesData" :value="category.id" :key="category.id">
            {{ category.name }}
          </option>
        </select>
      </div>
      <div>
        <label for="cooker">Nom du cuisinier :</label>
        <input type="text" id="cooker" v-model="form.cooker_name" />
      </div>
      <div>
        <label for="difficulty-select">Difficulté :</label>
        <select id="difficulties" v-model="form.difficulty_id">
          <option v-for="difficulty in difficultiesData" :value="difficulty.id" :key="difficulty.id">
            {{ difficulty.label }}
          </option>
        </select>
      </div>
      <div>
        <label for="photo">Photo de la recette :</label>
        <input type="url" id="photo" v-model="form.photo"/>
      </div>
      <div>
        <label for="timing">Durée de la recette :</label>
        <input type="time" id="timing" v-model="form.timing" min="00:00" max="50:00" required />
      </div>

      <div>
        <label for="ingredients">Ajout des ingrédients :</label>
        <div v-for="ingredient in ingredientsData" :key="ingredient.id">
          <input type="checkbox" :id="`ingredient-${ingredient.id}`" :value="ingredient.id" v-model="selectedIngredients"/>
          <p>{{ ingredient.name }}</p>
        </div>
      </div>

      <div>
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
          <input type="checkbox" :id="`tool-${tool.id}`" :value="tool.id" v-model="form.tools" />
          <p>{{ tool.name }}</p>
        </div>
      </div>

      <div>
        <label for="steps">Étapes :</label>
        <div v-for="(step, index) in Object.keys(form.steps)" :key="index">
          <div>
            <label>Titre de l'étape :</label>
            <input type="text" v-model="form.steps[step].title" />
          </div>
          <div>
            <label>Description de l'étape :</label>
            <input type="text" v-model="form.steps[step].description" />
          </div>
        </div>

        <button @click.prevent="addStep">Ajouter une étape</button>
      </div>

      <div>
        <input type="submit" value="Valider" />
      </div>
    </form>
  </main>
</template>

<script setup>
import { ref, reactive, watchEffect } from "vue";
import Navbar from "@/components/Navbar.vue";
import axios from "axios";

const categoriesData = ref([]);
const difficultiesData = ref([]);
const ingredientsData = ref([]);
const toolsData = ref([]);

const selectedIngredients = ref([]);
const selectedTools = ref([]);
const ingredientQuantities = reactive({});

const form = reactive({
  recipe_name: "",
  cooker_name: "",
  photo: "",
  category_id: "",
  difficulty_id: "",
  timing: "",
  ingredients: {},
  tools: [],
  steps: {
    1: { title: "", description: "" },
  }
});

function getCategories() {
  axios
  .get(`http://127.0.0.1:5000/categories`)
    .then((response) => {
      categoriesData.value = response.data;
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
    })
    .catch((error) => {
      console.error(error);
    });
}

function getIngredientName(ingredientId) {
  const ingredient = ingredientsData.value.find((item) => item.id === parseInt(ingredientId));
  return ingredient ? ingredient.name : "";
}

function getTools() {
  axios
  .get(`http://127.0.0.1:5000/tools`)
    .then((response) => {
      toolsData.value = response.data;
    })
    .catch((error) => {
      console.error(error);
    });
}
  
function addStep() {
  const newStepIndex = Object.keys(form.steps).length + 1;
  form.steps[newStepIndex] = reactive({ title: "", description: "" });
  console.log(form.steps);
}

// Surveiller les changements dans ingredientQuantities et mettre à jour la liste des ingrédients sélectionnés
watchEffect(ingredientQuantities);

function submitForm() {
  form.ingredients = {};
  selectedIngredients.value.forEach((ingredientId) => {
    form.ingredients[ingredientId] = ingredientQuantities[ingredientId];
  });
  form.tools = [...selectedTools.value];
  form.steps = { ...form.steps };

  axios
    .post("http://127.0.0.1:5000/recipe", form)
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
