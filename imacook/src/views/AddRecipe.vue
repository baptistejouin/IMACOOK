<template>
  <main>
    <Navbar class="dark" />

   
    <h2 class="title_add">Ajouter une recette</h2>

    <div v-if="successMessage" class="success-message">
      <p>{{ successMessage }}</p>
    </div>

    <form v-else @submit.prevent="submitForm" class="form_recette">

      <input class="form_recette-input" placeholder="Nom de la recette" type="text" id="name" v-model="form.name" />

      <input class="form_recette-input" placeholder="Nom du cuisinier" type="text" id="cooker" v-model="form.cooker" />

      <input class="form_recette-input" placeholder="Lien de la photo" type="url" id="photo" v-model="form.picture"/>

      <div class="form_recette-input form_recette-select">
        <label for="categories">Nom de la catégorie</label>
        <select id="categories" v-model="form.category_id">
          <option v-for="category in categoriesData" :value="category.id" :key="category.id">
            {{ category.name }}
          </option>
        </select>
      </div>

      <div class="form_recette-input form_recette-select">
        <label for="difficulty-select">Difficulté :</label>
        <select id="difficulties" v-model="form.difficulty_id">
          <option v-for="difficulty in difficultiesData" :value="difficulty.id" :key="difficulty.id">
            {{ difficulty.label }}
          </option>
        </select>
      </div>

      <div class="form_recette-input form_recette-time">
        <label for="timing">Durée de la recette (en minutes)</label>
        <input type="number" id="timing" placeholder="60" v-model="form.cooking_time_s" min="0" required/>
      </div>

      <div class="form_medium-title">
        <svg class="icon_title" viewBox="0 0 44 44" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M5.5 5.5V38.5H15.7V32.0999H12.5C11.1193 32.0999 10 30.9806 10 29.5999C10 28.2192 11.1193 27.0999 12.5 27.0999H15.7V20.7L12.5 20.7001C11.1193 20.7001 10 19.5808 10 18.2001C9.99998 16.8194 11.1193 15.7001 12.5 15.7001L15.6997 15.7V12.5C15.6997 11.1193 16.819 10 18.1997 10C19.5804 10 20.6997 11.1193 20.6997 12.5V15.7H27.1004V12.5C27.1004 11.1193 28.2197 10 29.6004 10C30.9811 10 32.1004 11.1193 32.1004 12.5V15.7H38.5V5.5H5.5ZM39.86 20.7C41.8705 20.7 43.5 19.0702 43.5 17.06V4.14C43.5 2.12977 41.8705 0.5 39.86 0.5H4.14C2.12968 0.5 0.5 2.12968 0.5 4.14V39.86C0.5 41.8705 2.12977 43.5 4.14 43.5H17.06C19.0702 43.5 20.7 41.8705 20.7 39.86V20.7H39.86Z" fill="#7F4F12"/></svg>        
        <h2>Renseigner les indispensables</h2>
      </div>

      <div class="form_recette-input">
        <div class="ingredients_container-title">
          <label for="ingredients_title">Sélectionner des ingrédients</label>
          <svg xmlns="http://www.w3.org/2000/svg" class="ionicon" viewBox="0 0 512 512"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="48" d="M112 184l144 144 144-144"/></svg>
        </div>

        <div class="drop_down-ingredients" style="height:0px;">
          <div v-for="ingredient in ingredientsData" :key="ingredient.id" class="ingredient_add">
            <input type="checkbox" :id="`ingredient-${ingredient.id}`" :value="ingredient.id" v-model="selectedIngredients"/>
            <p>{{ ingredient.name }}</p>
          </div>
        </div>
      </div>

      <div class="quantity_container">
        <div class="form_recette-input quantity" v-for="ingredientId in selectedIngredients" :key="ingredientId">
          <p>{{ getIngredient(ingredientId).name }} - Quantité :</p>
          <input type="text" size="5" v-model="ingredientQuantities[ingredientId]"/>
          <p>{{ getIngredient(ingredientId).unit }}</p>
        </div>
      </div>

      <div class="form_recette-input">
        <div class="ustensilles_container-title">
          <label for="ustensilless_title">Sélectionner des ustensiles</label>
          <svg xmlns="http://www.w3.org/2000/svg" class="ionicon" viewBox="0 0 512 512"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="48" d="M112 184l144 144 144-144"/></svg>
        </div>
        <div class="drop_down-ustensilles" style="height:0px;">
          <div v-for="tool in toolsData" :key="tool.id" class="ustensille_add">
            <input type="checkbox" :id="`tool-${tool.id}`" :value="tool.id" v-model="selectedTools"/>
            <p>{{ tool.name }}</p>
          </div>
        </div>
      </div>

      <div class="form_medium-title">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 69.6 64.1"><g id="Calque_2" data-name="Calque 2"><g id="Calque_1-2" data-name="Calque 1"><path class="cls-1" d="M64.39,58.92a2,2,0,0,1,0,2.83l-1.77,1.76a2,2,0,0,1-2.83,0l-23-23-23,23a2,2,0,0,1-2.82,0L9.2,61.75a2,2,0,0,1,0-2.83L40.59,27.53c-2.77-5.14-.79-13,5.14-19C52.53,1.74,62,.15,66.81,5s3.24,14.28-3.57,21.09c-5.45,5.45-12.61,7.56-17.72,5.69l-.1.12-4,4Z"/><path class="cls-1" d="M-3.82,11.42h36a2,2,0,0,1,2,2v9a2,2,0,0,1-2,2h-27a11,11,0,0,1-11-11v0a2,2,0,0,1,2-2Z" transform="translate(16.83 -4.79) rotate(45)"/></g></g></svg>
        <h2>Renseigner les étapes</h2>
      </div>

      <div class="form_steps">
        <div class="form_steps-infos" v-for="(step, index) in Object.keys(form.steps)" :key="index">
            <input class="form_recette-input" placeholder="Titre de l'étape" type="text" v-model="form.steps[step].title" />
            <textarea class="form_recette-input" placeholder="Description de l'étape" type="text" v-model="form.steps[step].description" ></textarea>
        </div>
        <button class="form_button" @click.prevent="addStep">Ajouter une étape</button>
      </div>

      <input class="form_button valider" type="submit" value="Ajouter la recette" />
    </form>
  </main>
</template>

<script setup>
import { ref, reactive, watchEffect, onMounted } from "vue";
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
  form.cooking_time_s = form.cooking_time_s*60;

  // check if all field is filled
  if (
    form.name === "" ||
    form.cooker === "" ||
    form.picture === "" ||
    form.category_id === "" ||
    form.difficulty_id === "" ||
    form.cooking_time_s === "" ||
    form.ingredients === {} ||
    form.tools === {} ||
    form.steps === {}
  ) {
    alert("Veuillez remplir tous les champs");
    return;
  }

  axios
    .post(`${API_ENDPOINT}/recipe`, form)
    .then((response) => {
      console.log("recipe created", response.data);
      successMessage.value = `La recette ${response.data.name} a été ajoutée avec succès !`;
    })
    .catch((error) => {
      console.error(error);
    });

    // With fetch api

    // fetch(`${API_ENDPOINT}/recipe`, {
    //   method: "POST",
    //   body: JSON.stringify(form),
    //   headers: {
    //     "Content-Type": "application/json",
    //   },
    // })
    //   .then((response) => response.json())
    //   .then((data) => {
    //     console.log("recipe created", data);
    //     successMessage.value = `La recette ${data.name} a été ajoutée avec succès !`;
    //   })
    //   .catch((error) => {
    //     console.error(error);
    //   });

}

getCategories();
getDifficulties();
getIngredients();
getTools();

onMounted(() => {
  const title = document.querySelector(".ingredients_container-title");
  const dropdown = document.querySelector(".drop_down-ingredients");
  const arrow = document.querySelector(".ingredients_container-title svg");

  function toggleDropdown() {
    if (dropdown.style.height === "0px") {
      dropdown.style.height = "180px";
      arrow.style.transform = "rotate(0deg)";
    } else {
      dropdown.style.height = "0px";
      arrow.style.transform = "rotate(180deg)";
    }
  }
  title.addEventListener("click", toggleDropdown);

  const title2 = document.querySelector(".ustensilles_container-title");
  const dropdown2 = document.querySelector(".drop_down-ustensilles");
  const arrow2 = document.querySelector(".ustensilles_container-title svg");

  function toggleDropdown2() {
    if (dropdown2.style.height === "0px") {
      dropdown2.style.height = "180px";
      arrow2.style.transform = "rotate(0deg)";
    } else {
      dropdown2.style.height = "0px";
      arrow2.style.transform = "rotate(180deg)";
    }
  }
  title2.addEventListener("click", toggleDropdown2);
})

</script>
