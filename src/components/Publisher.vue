<template>
  <v-container grid-list-md>
    <v-row >
      <v-col cols="12" sm="6">
        <v-card v-for="data in news" v-bind:key="data.date">
          <v-card-title>
          <div>{{data.date}}</div>
          </v-card-title>
          <v-card-text class="font-weight-bold ">{{data.title}}</v-card-text>
          <v-card-text class="font-weight-light">{{data.description}}</v-card-text>
          <v-card-actions>
            <v-btn  text color="teal accent-4" @click="reveal = true " :href="data.link">
            Learn More </v-btn></v-card-actions>
            <!-- <a :href="data.link">{{data.link}}</a></v-card-actions> -->
        </v-card>
        
      </v-col>
        <v-col cols="12" sm="6">
         <v-card v-for="data in news2" v-bind:key="data.date">
          <v-card-title>
          <div>{{data.date}}</div>
          </v-card-title>
          <v-card-text class="font-weight-bold">{{data.title}}</v-card-text>
          <v-card-text class="font-weight-light">{{data.description}}</v-card-text>
          <v-card-actions>
            <v-btn  text color="teal accent-4" @click="reveal = true " :href="data.link">
            Learn More </v-btn></v-card-actions>
            <!-- <a :href="data.link">{{data.link}}</a></v-card-actions> -->
        </v-card>
      </v-col>
    </v-row>
    
  </v-container>

</template>

<script>
import News from "../assets/news.json" 

import News2 from "../assets/Security_news.json"
export default {
  data() {
    return{
      news: News,
      news2: News2

    }
  }
}
</script>