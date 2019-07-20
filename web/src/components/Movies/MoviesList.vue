<template>
  <div class='movies-container'>
    <Movie v-for='movie in movies'
      :title='movie.title'
      :overview='movie.overview'
      :image='movie.image'
      :genres='movie.genres'
      :release_date='movie.release_date'  />
  </div>
</template>

<script>
import Movie from './Movie.vue';

export default {
  name: 'MoviesList',
  components: {
    Movie
  },
  data: () => { return {
    movies: []
  }},
  methods: {
    consumeData: function(movies) {
      movies.forEach(movie => { 
        movie.image = `http://image.tmdb.org/t/p/w342/${movie.image}`
        movie.release_date = movie.release_date;
      })
      this.movies = movies;
    }
  },
  mounted: async function() {
    let xmlHttp = new XMLHttpRequest();
    
    xmlHttp.onreadystatechange = () => { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200){
            this.consumeData(JSON.parse(xmlHttp.responseText));
        }
    }
    xmlHttp.open("GET", "http://127.0.0.1:5000/", true); 
    xmlHttp.send();
    
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
