<template>
  <main>
    <div
      class="header_recette"
      :style="`background-image: url('${recipeData.picture}');`"
    >
      <div class="header_recette-gradient"></div>
      <div class="header_recette-infos">
        <Navbar />
        <div class="header_recette-titre">
          <p>{{ recipeData.name }}</p>
        </div>
      </div>
    </div>
    <div class="tips_recette">
      <div class="tips_recette-content">
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
        <p>{{ parseInt(recipeData.cooking_time_s / 60) }} min</p>
      </div>
      <div class="tips_recette-content">
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
        <p>{{ recipeData.category }}</p>
      </div>
      <div class="tips_recette-content">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52.79 59.01">
          <g id="Calque_2" data-name="Calque 2">
            <g id="Calque_1-2" data-name="Calque 1">
              <path
                class="cls-1"
                d="M49.13,14.49a16.55,16.55,0,0,0-8-5.39,16.48,16.48,0,0,0-29.6.28A16.47,16.47,0,0,0,9.08,39.82v6.37a1.22,1.22,0,0,0,1.22,1.22h32a1.22,1.22,0,0,0,1.22-1.22V39.67a16.47,16.47,0,0,0,5.65-25.18Z"
              />
              <path
                class="cls-1"
                d="M42.26,52h-32a1.22,1.22,0,0,0-1.22,1.22V55a4,4,0,0,0,4,4H39.44a4,4,0,0,0,4-4V53.23A1.22,1.22,0,0,0,42.26,52Z"
              />
            </g>
          </g>
        </svg>
        <p>{{ recipeData.cooker }}</p>
      </div>
    </div>
    <div class="infos_recette">
      <div class="instructions_recette">
        <div class="instructions_title">
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
          <h2>Instructions</h2>
        </div>
        <div class="instructions_container">
          <div v-for="step in recipeData.steps" class="instruction">
            <p class="instrcution_index">{{ step.step_number }}</p>
            <div class="instruction_content">
              <h3>{{ step.title }}</h3>
              <p>{{ step.description }}</p>
            </div>
          </div>
        </div>
      </div>
      <div class="right_section">
        <div class="ingredients_recette">
          <div class="ingredients_title">
            <div class="title">
              <svg
                class="icon_title"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 69.87 69.69"
              >
                <g id="Calque_2" data-name="Calque 2">
                  <g id="Calque_1-2" data-name="Calque 1">
                    <path
                      class="cls-1"
                      d="M69.87,29.3a41.57,41.57,0,0,1-24.36,37,42.52,42.52,0,0,1-4,1.56c-.62.22-1.26.41-1.9.58a41.46,41.46,0,0,1-6.83,1.29h-.17a39.15,39.15,0,0,1-4.44-1.23c-.55-.18-1.1-.38-1.64-.59-1.13-.44-2.23-.91-3.25-1.41A41.12,41.12,0,0,1,0,29.25c0-.24,0-.46,0-.7a.48.48,0,0,1,.16-.35.49.49,0,0,1,.36-.13,41.08,41.08,0,0,1,23.25,8.5,40.94,40.94,0,0,1,7.15,7c.83,1,1.61,2.12,2.34,3.22A41.58,41.58,0,0,1,45.7,34.91a41.32,41.32,0,0,1,21.74-6.16c.65,0,1.3,0,1.94,0A.51.51,0,0,1,69.87,29.3Z"
                    />
                    <path
                      class="cls-1"
                      d="M46.71,25.12a.5.5,0,0,1-.22.47A40,40,0,0,0,35.16,36.53a.52.52,0,0,1-.41.21.49.49,0,0,1-.41-.21A40.44,40.44,0,0,0,22.7,25.41a.49.49,0,0,1-.23-.47A41.39,41.39,0,0,1,34.22.14a.51.51,0,0,1,.71,0A41.35,41.35,0,0,1,46.71,25.12Z"
                    />
                  </g>
                </g>
              </svg>
              <h2>Ingrédients</h2>
            </div>
            <div class="number_selector">
              <button id="removeGuest" @click="decrement">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 45.59 45.59"
                >
                  <g id="Calque_2" data-name="Calque 2">
                    <g id="Calque_1-2" data-name="Calque 1">
                      <path
                        class="cls-1"
                        d="M31.52,0H14.07A14.09,14.09,0,0,0,0,14.08V31.51A14.09,14.09,0,0,0,14.07,45.59H31.52A14.09,14.09,0,0,0,45.59,31.51V14.08A14.09,14.09,0,0,0,31.52,0ZM41,30.87A10.15,10.15,0,0,1,30.87,41H14.72A10.15,10.15,0,0,1,4.58,30.87V14.72A10.14,10.14,0,0,1,14.72,4.59H30.87A10.14,10.14,0,0,1,41,14.72Z"
                      />
                      <path
                        class="cls-2"
                        d="M32.28,22.53v.55a2.6,2.6,0,0,1-2.6,2.59H15.9a2.59,2.59,0,0,1-2.59-2.59v-.55a2.6,2.6,0,0,1,2.59-2.6H29.68A2.61,2.61,0,0,1,32.28,22.53Z"
                      />
                    </g>
                  </g>
                </svg>
              </button>
              <p class="guest">
                {{ count }} personne{{ count > 1 ? "s" : "" }}
              </p>
              <button id="addGuest" @click="increment">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 45.6 45.59"
                >
                  <g id="Calque_2" data-name="Calque 2">
                    <g id="Calque_1-2" data-name="Calque 1">
                      <path
                        class="cls-1"
                        d="M32.29,22.51v.55a2.61,2.61,0,0,1-2.6,2.6h-4v4a2.59,2.59,0,0,1-2.59,2.59h-.55a2.6,2.6,0,0,1-2.6-2.59v-4h-4a2.6,2.6,0,0,1-2.59-2.6v-.55a2.59,2.59,0,0,1,2.59-2.59h4v-4a2.61,2.61,0,0,1,2.6-2.6h.55a2.6,2.6,0,0,1,2.59,2.6v4h4A2.6,2.6,0,0,1,32.29,22.51Z"
                      />
                      <path
                        class="cls-2"
                        d="M31.52,0H14.08A14.09,14.09,0,0,0,0,14.08V31.51A14.09,14.09,0,0,0,14.08,45.59H31.52A14.09,14.09,0,0,0,45.6,31.51V14.08A14.09,14.09,0,0,0,31.52,0ZM41,30.87A10.14,10.14,0,0,1,30.88,41H14.72A10.14,10.14,0,0,1,4.59,30.87V14.72A10.14,10.14,0,0,1,14.72,4.59H30.88A10.14,10.14,0,0,1,41,14.72Z"
                      />
                    </g>
                  </g>
                </svg>
              </button>
            </div>
          </div>
          <div class="ingredients_container">
            <div
              v-for="ingredient in recipeData.ingredients"
              class="ingredient"
            >
              <p>{{ ingredient.name }}</p>
              <p class="strong">
                <span>{{ ingredient.quantity * count }}</span>
                {{ ingredient.unit }}
              </p>
            </div>
          </div>
        </div>

        <div class="ingredients_recette">
          <div class="ingredients_title">
            <div class="title">
              <svg
                class="icon_title"
                viewBox="0 0 44 44"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  clip-rule="evenodd"
                  d="M5.5 5.5V38.5H15.7V32.0999H12.5C11.1193 32.0999 10 30.9806 10 29.5999C10 28.2192 11.1193 27.0999 12.5 27.0999H15.7V20.7L12.5 20.7001C11.1193 20.7001 10 19.5808 10 18.2001C9.99998 16.8194 11.1193 15.7001 12.5 15.7001L15.6997 15.7V12.5C15.6997 11.1193 16.819 10 18.1997 10C19.5804 10 20.6997 11.1193 20.6997 12.5V15.7H27.1004V12.5C27.1004 11.1193 28.2197 10 29.6004 10C30.9811 10 32.1004 11.1193 32.1004 12.5V15.7H38.5V5.5H5.5ZM39.86 20.7C41.8705 20.7 43.5 19.0702 43.5 17.06V4.14C43.5 2.12977 41.8705 0.5 39.86 0.5H4.14C2.12968 0.5 0.5 2.12968 0.5 4.14V39.86C0.5 41.8705 2.12977 43.5 4.14 43.5H17.06C19.0702 43.5 20.7 41.8705 20.7 39.86V20.7H39.86Z"
                  fill="#7F4F12"
                />
              </svg>

              <h2>Ustensile</h2>
            </div>
          </div>
          <div class="ingredients_container">
            <div v-for="tool in recipeData.tools" class="ingredient">
              <p>{{ tool.name }}</p>
              <p class="strong">
                <span>{{ tool.quantity }}</span> {{ tool.unit }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from "vue";
import { API_ENDPOINT } from "@/app.config.js";
import Navbar from "@/components/Navbar.vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";

const route = useRoute();
const router = useRouter();
const recipeId = route.params.id;

const recipeData = ref([]);
const count = ref(1);

function getData() {
  axios
    .get(`${API_ENDPOINT}/recipe/${recipeId}`)
    .then((response) => {
      recipeData.value = response.data;
      console.log(response.data);
    })
    .catch((error) => {
      console.error(error);
      // redirect to 404
      router.push({ path: "/404" });
    });
}

function increment() {
  count.value++;
}
function decrement() {
  if (count.value > 1) {
    count.value--;
  }
}

getData();
</script>

<style scoped>
.right_section {
  width: 46%;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
.header_recette {
  width: 100%;
  position: relative;
  background: black;
  border-radius: 60px;
  background-size: cover;
  background-repeat: no-repeat;
  height: 400px;
}
.header_recette-gradient {
  border-radius: 60px;
  position: absolute;
  width: 100%;
  height: 100%;
  background: rgb(0, 0, 0);
  background: linear-gradient(
    0deg,
    rgba(0, 0, 0, 0.4962359943977591) 0%,
    rgba(0, 0, 0, 0) 40%,
    rgba(0, 0, 0, 0) 70%,
    rgba(0, 0, 0, 0.4962359943977591) 100%
  );
}
.header_recette-infos {
  padding: var(--padding);
  align-content: space-between;
  position: absolute;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  align-items: space-between;
}
.header_recette-titre {
  width: 100%;
  display: flex;
  justify-content: flex-start;
}
.header_recette-titre p {
  font-family: var(--regular-font);
  font-size: var(--big-font-size);
  color: var(--second-color);
  text-decoration: none;
  font-weight: 600;
}

.tips_recette {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin: 25px 0px 50px 0px;
}
.tips_recette-content {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}
.tips_recette-content svg {
  fill: var(--first-color);
  width: var(--icon_min_height);
  height: var(--icon_min_height);
  margin: 0px 8px 0px 0px;
}
.tips_recette-content p {
  font-family: var(--regular-font);
  font-size: var(--normal-font-size);
  color: var(--first-color);
  text-decoration: none;
  font-weight: 600;
  margin: 0px 50px 0px 0px;
}

.infos_recette {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  flex-wrap: wrap;
  margin: 25px 0px;
}
.instructions_recette {
  width: 46%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: wrap;
}
.instructions_title {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
}
.instructions_title svg {
  width: var(--icon_max_height);
  height: var(--icon_max_height);
  fill: var(--first-color);
  margin: 0px 8px 0px 0px;
}
.instructions_title h2 {
  font-family: var(--regular-font);
  font-size: var(--medium-font-size);
  color: var(--first-color);
  text-decoration: none;
  font-weight: 700;
}
.instructions_container {
  margin: 20px 0px 0px 0px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  flex-wrap: wrap;
}
.instruction {
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  width: 100%;
  margin-bottom: 25px;
}
.instrcution_index {
  background-color: var(--fourth-color);
  border-radius: 50%;
  min-width: var(--icon_max_height);
  height: var(--icon_max_height);
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: var(--regular-font);
  font-size: var(--medium-font-size);
  color: var(--first-color);
  font-weight: 700;
}
.instruction_content {
  margin: 0px 0px 0px 20px;
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: flex-start;
}
.instruction_content h3 {
  font-family: var(--regular-font);
  font-size: var(--normal-font-size);
  color: var(--first-color);
  margin: 0px 0px 5px 0px;
  font-weight: 700;
}
.instruction_content p {
  font-family: var(--regular-font);
  font-size: var(--normal-font-size);
  color: var(--first-color);
}
.ingredients_recette {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: wrap;
}
.ingredients_title {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.ingredients_title .title {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}
.ingredients_title .title svg {
  width: var(--icon_normal_height);
  height: var(--icon_normal_height);
  fill: var(--first-color);
  margin: 0px 8px 0px 0px;
}
.ingredients_title .title h2 {
  font-family: var(--regular-font);
  font-size: var(--medium-font-size);
  color: var(--first-color);
  text-decoration: none;
  font-weight: 700;
}
.number_selector {
  display: flex;
  align-items: center;
}
.number_selector p {
  font-family: var(--regular-font);
  font-size: var(--normal-font-size);
  color: var(--first-color);
  margin: 0px 10px;
  font-weight: 700;
}
.number_selector button {
  width: var(--icon_min_height);
  height: var(--icon_min_height);
  cursor: pointer;
  outline: none;
  border: none;
}
.number_selector button svg {
  fill: var(--first-color);
}
.ingredients_container {
  width: 100%;
  margin: 20px 0px 0px 0px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  flex-wrap: wrap;
}
.ingredient {
  padding: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  margin-bottom: 15px;
  border-radius: var(--button-radius);
  background-color: white;
  box-shadow: rgba(149, 157, 165, 0.08) 0px 8px 24px;
}
.ingredient p {
  font-family: var(--regular-font);
  font-size: var(--normal-font-size);
  color: var(--first-color);
  font-weight: 100;
}
.ingredient .strong {
  font-weight: 600;
}
</style>
