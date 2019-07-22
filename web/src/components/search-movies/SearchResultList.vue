<template>
    <div class='movies-container'>
        <MovieCard v-for='movie in movies' :movie='movie' />
    </div>
</template>

<script>
import MovieCard from  '../movie/MovieCard.vue';

export default {
    name: 'SearchResultList',
    components: {
        MovieCard
    },
    data: () => {
        return {
            movies: []
        }
    },
    methods: {
        requestPageFromServer(query) {
            const xmlHttp = new XMLHttpRequest();
            xmlHttp.onreadystatechange = () => {
                if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
                    this.consumeData(JSON.parse(xmlHttp.responseText));
                }
            }
            xmlHttp.open("GET", `https://immense-brook-71998.herokuapp.com/search?query=${query}`, true);
            xmlHttp.send();
        },
        consumeData: function(movies) {
            movies.forEach(movie => {
                movie.id = movie.id.toString();
                movie.image = `http://image.tmdb.org/t/p/w342/${movie.image}`
                movie.release_date = movie.release_date;
            });
            this.movies = [].concat(this.movies, movies);
        }
    },
    mounted: async function() {
        this.requestPageFromServer(this.$route.params.query);
    }
}
</script>

<style scoped>
.movies-container {
    display: flex;
    flex-wrap: wrap;
    margin: auto auto;
}
</style>
