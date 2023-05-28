<template>
  <main>
    <Navbar class="dark" />

    <section>
      <div class="titre">
        <h2>Ajout d'une recette</h2>
      </div>

      <div v-if="successMessage" class="success-message">
        <p>{{ successMessage }}</p>
      </div>

      <form v-else @submit.prevent="submitForm">
        <div class="form-step">
          <label for="name">Nom de la recette :</label>
          <input type="text" id="name" v-model="form.name" />
        </div>
        <div class="form-step">
          <label for="categories">Catégorie :</label>
          <select id="categories" v-model="form.category_id">
            <option
              v-for="category in categoriesData"
              :value="category.id"
              :key="category.id"
            >
              {{ category.name }}
            </option>
          </select>
        </div>
        <div class="form-step">
          <label for="cooker">Nom du cuisinier :</label>
          <input type="text" id="cooker" v-model="form.cooker" />
        </div>
        <div class="form-step">
          <label for="difficulty-select">Difficulté :</label>
          <select id="difficulties" v-model="form.difficulty_id">
            <option
              v-for="difficulty in difficultiesData"
              :value="difficulty.id"
              :key="difficulty.id"
            >
              {{ difficulty.label }}
            </option>
          </select>
        </div>
        <div class="form-step">
          <label for="photo">Photo de la recette :</label>
          <input type="url" id="photo" v-model="form.picture" />
        </div>
        <div>
          <label for="timing">Durée de la recette (en seconde):</label>
          <input
            type="number"
            id="timing"
            v-model="form.cooking_time_s"
            min="0"
            required
          />
        </div>

        <div class="form-step">
          <label for="ingredients">Ajout des ingrédients :</label>
          <div
            v-for="ingredient in ingredientsData"
            :key="ingredient.id"
            class="input-inline"
          >
            <input
              type="checkbox"
              :id="`ingredient-${ingredient.id}`"
              :value="ingredient.id"
              v-model="selectedIngredients"
            />
            <p>{{ ingredient.name }}</p>
          </div>
        </div>

        <div class="form-step">
          <label for="selectedIngredients">Quantité des ingrédients :</label>
          <div
            v-for="ingredientId in selectedIngredients"
            :key="ingredientId"
            class="input-inline"
          >
            <p>{{ getIngredient(ingredientId).name }}</p>
            <input
              type="text"
              size="5"
              v-model="ingredientQuantities[ingredientId]"
            />
            <p>{{ getIngredient(ingredientId).unit }}</p>
          </div>
        </div>

        <div class="form-step">
          <label for="tools">Ajout des ustensiles :</label>
          <div v-for="tool in toolsData" :key="tool.id" class="input-inline">
            <input
              type="checkbox"
              :id="`tool-${tool.id}`"
              :value="tool.id"
              v-model="selectedTools"
            />
            <p>{{ tool.name }}</p>
          </div>
        </div>

        <div class="form-step">
          <label for="steps">Étapes :</label>
          <div
            v-for="(step, index) in Object.keys(form.steps)"
            :key="index"
            class="step"
          >
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

        <div class="form-step">
          <input type="submit" value="Valider" />
        </div>
      </form>
    </section>
  </main>
</template>

<script setup>
import { ref, reactive, watchEffect } from "vue";
import { API_ENDPOINT } from "@/app.config.js";
import Navbar from "@/components/Navbar.vue";
import axios from "axios";

const categoriesData = ref([]);
const difficultiesData = ref([]);
const ingredientsData = ref([]);
const toolsData = ref([]);
const successMessage = ref("");

const selectedIngredients = ref([]);
const selectedTools = ref([]);
const ingredientQuantities = reactive({});

// log env variable

const form = reactive({
  name: "",
  cooker: "",
  picture: "",
  category_id: "",
  difficulty_id: "",
  cooking_time_s: "",
  ingredients: {},
  tools: {},
  steps: {
    1: { title: "", description: "" },
  },
});

function getCategories() {
  axios
    .get(`${API_ENDPOINT}/categories`)
    .then((response) => {
      categoriesData.value = response.data;
    })
    .catch((error) => {
      console.error(error);
    });
}

function getDifficulties() {
  axios
    .get(`${API_ENDPOINT}/difficulties`)
    .then((response) => {
      difficultiesData.value = response.data;
    })
    .catch((error) => {
      console.error(error);
    });
}

function getIngredients() {
  axios
    .get(`${API_ENDPOINT}/ingredients`)
    .then((response) => {
      ingredientsData.value = response.data;
    })
    .catch((error) => {
      console.error(error);
    });
}

function getIngredient(ingredientId) {
  const ingredient = ingredientsData.value.find(
    (item) => item.id === parseInt(ingredientId)
  );
  return ingredient ? ingredient : "";
}

function getTools() {
  axios
    .get(`${API_ENDPOINT}/tools`)
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
}

// Surveiller les changements dans ingredientQuantities et mettre à jour la liste des ingrédients sélectionnés
watchEffect(ingredientQuantities);

function submitForm() {
  const ingredients = selectedIngredients.value.map((ingredientId) => {
    return {
      id: ingredientId,
      quantity: ingredientQuantities[ingredientId],
    };
  });
  const tools = selectedTools.value.map((toolId) => {
    return {
      id: toolId,
    };
  });
  const steps = Object.keys(form.steps).map((stepNumber) => {
    const step = form.steps[stepNumber];
    return {
      step_number: parseInt(stepNumber),
      title: step.title,
      description: step.description,
    };
  });
  
  form.ingredients = ingredients;
  form.tools = tools;
  form.steps = steps;

  axios
    .post(`${API_ENDPOINT}/recipe`, form)
    .then((response) => {
      console.log("recipe created", response.data);
      successMessage.value = `La recette ${response.data.name} a été ajoutée avec succès !`;
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

<style scoped>
.input-inline {
  display: flex;
  align-items: center;
  gap: 0.5em;
}
.form-step {
  margin-block: 1rem;
}
section {
  display: flex;
  flex-direction: column;
}
.step {
  margin-bottom: 1rem;
}
</style>
