<template>
    <div class='movie-container'>
    <img class='movie-poster' :src='movie.image' />
      <h1 class='movie-title'> {{movie.title}}</h1>
      <div class='movie-details'>
        <span>  {{movie.overview}}</span>
        <span>  {{movie.genres}}</span>
        <span> Release date: {{movie.release_date}}</span>
      </div>
    </div>
</template>

<script>
export default {
  name: 'Movie',
  data: () => { return {
    movie: Object
  }},
  methods: {
    consumeData: function(movie) {
        movie.id = movie.id.toString();
        movie.image = `http://image.tmdb.org/t/p/w780/${movie.image}`
        movie.release_date = movie.release_date;
        movie.genres = movie.genres.slice(0, 3).join(', ');
        this.movie = movie;
    }
  },
  mounted: async function() {
    let xmlHttp = new XMLHttpRequest();
    
    xmlHttp.onreadystatechange = () => { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200){
            this.consumeData(JSON.parse(xmlHttp.responseText));
        }
    }
    xmlHttp.open("GET", `http://127.0.0.1:5000/movieDetails?id=${this.$route.params.id}`, true); 
    xmlHttp.send();
  }
}
</script>

<style scoped>
.movie-container {
    display: grid;
    grid-template-columns: 40% 60%;
    height: 70%;
    width: 70%;
    font-family: 'Montserrat';
    background-color: rgb(240, 240, 240);
    margin: 1% auto 1% auto;
}

.movie-poster {
    grid-column: 1/1;
    grid-row: 1/4;
    object-fit: cover;
    width: 100%;
    max-height: 100%;
}

.movie-title {
  background-color: rgb(200, 200, 200);
  color: white;
  margin: 0;
  text-align: center;
  padding: 0px 10px;
  grid-column: 2/2;
}

.movie-details {
    padding: 10px;
    display: grid;
}

span {
  padding-bottom: 10px;
}
</style>
