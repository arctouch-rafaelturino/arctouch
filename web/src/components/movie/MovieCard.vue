<template>
    <router-link :to="'/movie/' + movie.id" class='movie-card'>
        <img class='movie-poster' :src='movie.image' />
        <h3 class='movie-title'> {{movie.title}}</h3>
        <div class='movie-details'>
            <span>  {{movie.genres.slice(0, 3).join(', ')}}</span>
            <span> Release date: {{movie.release_date}}</span>
        </div>
    </router-link>
</template>

<script>
export default {
    name: 'MovieCard',
    props: {
        movie: Object
    }
}
</script>

<style scoped>
a {
    color: black;
}

.movie-card {
    display: grid;
    grid-template-columns: auto;
    grid-template-rows: 6fr 1fr 1fr 1fr;
    width: 300px;
    font-family: 'Montserrat';
    background-color: rgb(240, 240, 240);
    margin: 30px;
}

.movie-poster {
    grid-column: 1/1;
    grid-row: 1/4;
    width: 100%;
}

.movie-title {
    background-color: rgb(200, 200, 200);
    color: white;
    display:flex;
    align-items: center;
    justify-content: center;
    margin: 0;
    padding: 0px 10px;
}

.movie-details {
    padding: 10px;
    display: grid;
}
</style>
