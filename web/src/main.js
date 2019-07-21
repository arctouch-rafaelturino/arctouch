import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from './Home.vue';
import Movie from './components/movie/Movie.vue';
import UpcomingMoviesList from './components/upcoming-movies/UpcomingMoviesList.vue';
import SearchResultList from './components/search-movies/SearchResultList.vue';

Vue.config.productionTip = false

const routes =  [
  { path: '/', component: UpcomingMoviesList },
  { path: '/search/:query', component: SearchResultList },
  { path: '/movie/:id', component: Movie}
];
const router = new VueRouter({
  routes, linkActiveClass: '', linkExactActiveClass: ''});

Vue.use(VueRouter) 

new Vue({
  render: h => h(Home), 
  router
}).$mount('#app')
