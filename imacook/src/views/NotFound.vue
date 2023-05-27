<template>
	<main>

		<Navbar class="dark"/>
<div class="notfound">

	<h1>404</h1>
	<p>La page n'existe pas ou à été supprimée.</p>
	<router-link to="/">Retour à la page d'accueil</router-link>
</div>
	</main>
</template>
<script setup>
import Navbar from "@/components/Navbar.vue";

</script>
<style scoped>
.notfound {
	width: 100%;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	gap: 1rem;
}
</style>