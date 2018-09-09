import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import router from './router'
import axios from 'axios'
import config from './config'
Vue.prototype.$http = axios
Vue.prototype.$serverUrl = config.serverUrl;

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
