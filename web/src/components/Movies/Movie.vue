<template>
  <div class='movie-card'>
  <img class='movie-poster' :src='image'></span>
  <h3 class='movie-title'> {{title}}</h3>
  <div class='movie-details'>
  <span>  {{genres.slice(0, 3).join(', ')}}</span>
  <span> Release date: {{release_date}}</span>
    </div>
 </div>
</template>

<script>
export default {
  name: 'Movie',
  props: {
      title: String,
      overview: String,
      image: String,
      genres: Array,
      release_date: String
  }
}
</script>

<style scoped>
.movie-card {
    display: grid;
    grid-template-columns: auto;
    grid-template-rows: 5fr 1fr 1fr 1fr;
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
  margin: 0;
  text-align: center;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  padding: 0px 10px;
}

.movie-details {
    padding: 10px;
    display: grid;
}
</style>
