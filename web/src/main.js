import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './Home.vue'

Vue.config.productionTip = false

const routes =  [{ path: '/home', component: Home }];
const router = new VueRouter({
  routes, linkActiveClass: '', linkExactActiveClass: ''});

Vue.use(VueRouter) 

new Vue({
  render: h => h(Home), 
  router
}).$mount('#app')
