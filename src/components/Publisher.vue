<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card v-for="data in news" v-bind:key="data.news">
          <div>{{data}}</div>
          
        </v-card>
      </v-col>
        <v-col>
          <v-card>
          test
        </v-card>
      </v-col>
    </v-row>
    
  </v-container>

</template>

<script>
import Publisher from "../assets/news.json"

export default {
  data() {
    return{
      news: Publisher
    }
  }
}
</script>