<template>
  <div id="app">
    <v-app>
      <v-main>
        <!-- <my-header /> -->
        <v-container>
          <router-view/>
        </v-container>
      </v-main>
    </v-app>

  </div>
</template>

<script>
import MyHeader from '@/components/Header'

export default {
  name: 'App',
  components: {
    MyHeader
  }
}
</script>

<style src="vue-material/dist/vue-material.css"></style>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>