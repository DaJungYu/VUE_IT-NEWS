<template>
  <v-container grid-list-md>
    <v-row >
      <!--Security_News-->
      <v-col cols="12" sm="6"> 
        <v-card v-for="data in news" v-bind:key="data.id">
          <!-- <v-img v-bind:src="data.image" height="200px" align="left"  class="white--text align-end"> -->
          <v-img :src="`http://127.0.0.1:5000/static/image_sec/${data.id}.jpg`" height="200px" align="left"  class="white--text align-end">
            <div class="d-inline pa-2 black white--text">{{data.date.split(' ')[0]}}</div>
            <!-- <v-card-text class="font-weight-bold ">{{data.date.split(' ')[0]}}</v-card-text> -->
          </v-img>
          
          <v-card-text class="text-h6 font-weight-bold " color="black">{{data.title}}</v-card-text>
          <!--
          <v-img :src="'/D:\해킹스터디\프로젝트\flask\crawling\image_sec' + data.id"></v-img>-->
          <v-card-text class="font-weight-light">{{data.description}}</v-card-text>
          <v-card-actions>
            <v-btn  text color="teal accent-4" @click="reveal = true " :href="data.link">
            Read More </v-btn></v-card-actions>
            <!-- <a :href="data.link">{{data.link}}</a></v-card-actions> -->
        </v-card>
        
      </v-col>
      <!--Naver_News-->
        <v-col cols="12" sm="6">
         <v-card v-for="data in news2" v-bind:key="data.id">
          <v-img :src="`http://127.0.0.1:5000/static/image/${data.id}.jpg`" height="200px" align="left"  class="white--text align-end">
            <div class="d-inline pa-2 black white--text">{{data.date.split(' ')[0]}}</div>
          </v-img>
          <v-card-text class="text-h6 font-weight-bold">{{data.title}}</v-card-text>
          <v-card-text class="font-weight-light">{{data.description}}</v-card-text>
          <v-card-actions>
            <v-btn  text color="orange lighten-2" @click="reveal = true " :href="data.link">
            Read More </v-btn></v-card-actions>
            <!-- <a :href="data.link">{{data.link}}</a></v-card-actions> -->
        </v-card>
      </v-col>
    </v-row>
    
  </v-container>

</template>


<script>
// axios
import api from '@/api'


export default {
  data() {
    return{
      news: [], //처음에 빈 배열 (security)
      news2: [] //처음에 빈 배열 (naver)
    }
  },
  
  methods: {
    getMydata(){ 
      api.get('/security_news').then(res => {
        this.news = res.data; // news 데이터 받아옴.
      }).catch((error)=>{
        console.error(error);
      });
    },
    getMydata2(){
      api.get('/naver_news').then(res => {
        this.news2 = res.data; // news2 데이터 받아옴.
      }).catch((error)=>{
        console.error(error);
      });
    },
  },
  created() {
    this.getMydata();
    this.getMydata2();
  },
}

// export const actions = {
//   axios({commit}){
//     this.$axios.get('http://127.0.0.1:5000/security_news'.format(path)).then(res=>{
//       this.security_news=res.data;
//       //commit('News',c.data);
//     });
 

</script>