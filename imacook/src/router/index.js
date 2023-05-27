import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import Recipe from "@/views/Recipe.vue";
import AddRecipe from "@/views/AddRecipe.vue";
import Search from "@/views/Search.vue";
import NotFound from "@/views/NotFound.vue";

const routes = [
  { path: "/", name: "Home", component: Home },
  { path: "/add", name: "AddRecipe", component: AddRecipe },
  { path: "/search", name: "Search", component: Search },
  { path: "/recipe/:id", name: "Recipe", component: Recipe },
  { path: "/:pathMatch(.*)*", alias: ["/404"], component: NotFound },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
