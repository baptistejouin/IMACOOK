<template>
	<div class="navbar">
        <a class="logo" href="/">IMACook</a>
        <div class="links">
            <a href="/">Accueil</a>
        </div>
        <div class="icon">
            <a class="icon_svg" href="/search">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 67.25 64.86"><g id="Calque_2" data-name="Calque 2"><g id="Calque_1-2" data-name="Calque 1"><path class="cls-1" d="M66.48,60.27l-15-15a28.64,28.64,0,1,0-3.6,4l14.8,14.8a2.67,2.67,0,0,0,3.76,0l.06-.06A2.67,2.67,0,0,0,66.48,60.27ZM28.47,51A22.55,22.55,0,1,1,51,28.47,22.55,22.55,0,0,1,28.47,51Z"/></g></g></svg></a>
            <a class="icon_svg" href="/add">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 45.59 45.58"><g id="Calque_2" data-name="Calque 2"><g id="Calque_1-2" data-name="Calque 1"><path class="cls-1" d="M32.29,22.51v.55a2.61,2.61,0,0,1-2.6,2.6h-4v4a2.59,2.59,0,0,1-2.59,2.59h-.55a2.6,2.6,0,0,1-2.6-2.59v-4h-4a2.6,2.6,0,0,1-2.59-2.6v-.55a2.59,2.59,0,0,1,2.59-2.59h4v-4a2.61,2.61,0,0,1,2.6-2.6h.55a2.6,2.6,0,0,1,2.59,2.6v4h4A2.6,2.6,0,0,1,32.29,22.51Z"/><path class="cls-1" d="M31.52,0H14.07A14.09,14.09,0,0,0,0,14.07V31.51A14.09,14.09,0,0,0,14.07,45.58H31.52A14.09,14.09,0,0,0,45.59,31.51V14.07A14.09,14.09,0,0,0,31.52,0ZM41,30.86A10.15,10.15,0,0,1,30.87,41H14.72A10.14,10.14,0,0,1,4.59,30.86V14.72A10.14,10.14,0,0,1,14.72,4.59H30.87A10.14,10.14,0,0,1,41,14.72Z"/></g></g></svg>
            </a>
        </div>
    </div>
</template>

<style scoped>
.navbar{
    display: flex;
    width: 100%;
    justify-content: space-between;
    align-items: center;
}
.logo{
    font-family:var(--regular-font);
    font-size:var(--medium-font-size);
    color:var(--second-color);
    text-decoration: none;
    font-weight: 600;
}
.links a{
    font-family:var(--regular-font);
    font-size:var(--normal-font-size);
    color:var(--second-color);
    text-decoration: none;
    margin:0px 25px;
}
.icon{
    display: flex;
    justify-content: space-between;
}
.icon_svg svg{
    width:var(--icon_min_height);
    height:var(--icon_min_height);
    margin:0px 0px 0px 30px;
    fill:var(--second-color);
}
</style>

<script>
export default {
	name: 'Navbar'
};
</script>