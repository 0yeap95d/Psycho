import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import infiniteScroll from 'vue-infinite-scroll';
import router from './router';
import store from './store';
import Carousel3d from 'vue-carousel-3d';

Vue.config.productionTip = false;
Vue.use(infiniteScroll);
Vue.use(Carousel3d);

new Vue({
  vuetify,
  router,
  store,
  render: (h) => h(App)
}).$mount('#app');
