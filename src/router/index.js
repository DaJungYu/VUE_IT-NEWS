import Vue from 'vue'
import Router from 'vue-router'
import Header from '@/components/Header'
import News from '@/components/News'
import Publisher from '@/components/Publisher'

Vue.use(Router);

export default new Router({
  routes: [
    // {
    //   // Homepage
    //   path: '/',
    //   name: 'Header',
    //   component: Header
    // },
    {
      // Publisher List
      path: '/',
      name: 'Publisher',
      components: {
        default: Publisher,

      }
    },
    {
      // News List
      path: '/News',
      name: 'News',
      components: {
        default: News,

      }
    },
    // {
    //   // Display selected publisher news
    //   path: '/news/:id',
    //   name: 'News',
    //   component: News
    // }
  ]
});