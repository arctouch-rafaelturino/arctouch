<template>
    <div class='movies-container'>
        <MovieCard v-for='movie in movies' :movie='movie' />
    </div>
</template>

<script>
import MovieCard from  '../movie/MovieCard.vue';

export default {
    name: 'UpcomingMoviesList',
    components: {
        MovieCard
    },
    data: () => {
        return {
            currentPage: 1,
            movies: []
        }
    },
    methods: {
        requestPageFromServer(page) {
            let xmlHttp = new XMLHttpRequest();
            xmlHttp.onreadystatechange = () => {
                if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
                    this.consumeData(JSON.parse(xmlHttp.responseText));
                }
            }
            xmlHttp.open("GET", `http://127.0.0.1:5000/upcomingMovies?page=${page}`, true);
            xmlHttp.send();
        },
        consumeData: function(movies) {
            movies.forEach(movie => {
                movie.id = movie.id.toString();
                movie.image = `http://image.tmdb.org/t/p/w342/${movie.image}`
                movie.release_date = movie.release_date;
            });
            this.movies = [].concat(this.movies, movies);
        },
        checkScroll: function() {
            window.onscroll = () => {
                const bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight;
                if (bottomOfWindow) {
                    this.currentPage = this.currentPage + 1;
                    this.requestPageFromServer(this.currentPage);
                }
            }
        }
    },
    mounted: async function() {
        this.requestPageFromServer(this.currentPage);
        this.checkScroll();
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
