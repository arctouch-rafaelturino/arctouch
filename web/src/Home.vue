<template>
  <div id="home">
    <div class="banner">
      <router-link to="/home">
      <span class="page-title">my thursday night</span>
      </router-link>
    </div>
    <Search />
    <MoviesList/>
  </div>
</template>

<script>
import VueRouter from 'vue-router';
import Search from './components/Search.vue'
import MoviesList from './components/Movies/MoviesList.vue'

export default {
  name: 'home',
  components: {
    MoviesList,
    Search
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Montserrat:400,700&display=swap');

html, body, #app {
  padding: 0;
  margin: 0;
}

a {
  text-decoration: none;
}

#app {
  width: 100%;
}
.banner {
  background-image: linear-gradient(to right, rgb(255,140,50), rgb(250,100,0));
  width: 100%;
  font-family: 'Montserrat', sans-serif;
  text-align: center;
  font-weight: bold;
  padding: 20px 0;

}

.page-title {
  font-size: 2em;
  color: white;

}
</style>
